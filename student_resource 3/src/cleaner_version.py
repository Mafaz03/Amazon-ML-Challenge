import os
import pandas as pd
import easyocr
import ssl
import requests
from PIL import Image
import re
import constants
from constants import unit_abbreviation_map


def ocr(img_link):
    reader = easyocr.Reader(['en'])
    get_from_net = requests.get(img_link, stream=True).raw
    image = Image.open(get_from_net)
    texts = reader.readtext(image)
    return texts

def clean1(texts):
    new_entries = []
    to_delete = []

    # Function to clean and normalize the input
    def clean_and_normalize(value):
        # Replace comma with period
        return value.replace(',', '.')

    # Loop over the list using enumerate to track index
    for i, text in enumerate(texts):
        # Check if '/' is in text[1]
        if '/' in text[1]:
            # Clean and normalize the text[1]
            cleaned_text = clean_and_normalize(text[1])
            # Split the cleaned text[1] by '/'
            todo = cleaned_text.split('/')
            
            # Add each part as a new tuple
            for k in todo:
                new_entries.append(
                    (text[0], k.strip(), text[-1])
                )
            
            # Mark the original entry for deletion
            to_delete.append(i)

    # Remove the original entries from texts in reverse order to avoid index issues
    for index in sorted(to_delete, reverse=True):
        del texts[index]

    # Extend the original texts list with the new entries
    texts.extend(new_entries)

    texts_dict = [{"text": text[1], "pred": text[-1]} for text in texts]
    texts_dict
    return texts_dict

def extract_and_replace_units(text, units_dict):
    # Create a regex pattern to match metrics and units
    pattern = r'(\d+\.?\d*)\s*(' + '|'.join(re.escape(key) for key in units_dict.keys()) + r')\b'
    
    # Find matches
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    
    # Extract metric and unit
    extracted_units = [{'metric': match[0], 'unit': units_dict.get(match[1].lower(), match[1])} for match in matches]
    
    # Replace units in the text
    def replace_match(match):
        return f"{match.group(1)} {units_dict.get(match.group(2).lower(), match.group(2))}"
    
    updated_text = re.sub(pattern, replace_match, text, flags=re.IGNORECASE)
    
    return {'text': updated_text, 'extracted_units': extracted_units}


# Function to normalize units
def normalize_unit(unit, entity_name):
    return unit_abbreviation_map[entity_name].get(unit.lower(), unit)

# Function to convert input to standardized form
def convert_to_standard_form(input_str, entity_name):
    # Regex to capture number and unit (with or without space between them)
    match = re.match(r"([0-9.]+)\s*([a-zA-Z]+)", input_str)
    if match:
        value = match.group(1)
        unit = match.group(2)
        
        # Normalize unit
        normalized_unit = normalize_unit(unit, entity_name)
        
        # Return standardized form: number + normalized unit
        return f"{value} {normalized_unit}"
    
    # If no match, return the input string unchanged
    return input_str

def is_unit_in_list(input_str, unit_list):
    # Regex to capture number and unit (ignoring the number here)
    match = re.match(r"([0-9.]+)\s*([a-zA-Z\s]+)", input_str)
    if match:
        unit = match.group(2).strip()
        # Normalize the unit
        normalized_unit = normalize_unit(unit)
        # Check if the normalized unit is in the provided list
        return normalized_unit in unit_list
    return False

def isin(string, words):
    pattern = '|'.join(re.escape(word) for word in words)
    if re.search(pattern, string):
        return True
    else:
        return False
    
def extract_and_format(text):
    # Define a regex pattern to match the numeric part and the unit
    pattern = r'(\d+\.?\d*)\s*([a-zA-Z]+)'
    
    # Find the match
    match = re.search(pattern, text)
    
    if match:
        # Extract numeric part and unit
        numeric_part = float(match.group(1))  # Convert to float
        unit = match.group(2)
        return numeric_part, unit
    else:
        return None, None
    
