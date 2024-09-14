entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'maximum_weight_recommendation': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centilitre',
        'cubic foot',
        'cubic inch',
        'cup',
        'decilitre',
        'fluid ounce',
        'gallon',
        'imperial gallon',
        'litre',
        'microlitre',
        'millilitre',
        'pint',
        'quart'}
}

unit_abbreviation_map = {
    "width": {'cm': 'centimetre',
    'ft': 'foot',
    'in': 'inch',
    'm': 'metre',
    'mm': 'millimetre',
    'yd': 'yard',
    '"': 'inch',}, 

    "depth": {'cm': 'centimetre',
    'ft': 'foot',
    'in': 'inch',
    'm': 'metre',
    'mm': 'millimetre',
    'yd': 'yard',
    '"': 'inch',},

    "height": {'cm': 'centimetre',
    'ft': 'foot',
    'in': 'inch',
    'm': 'metre',
    'mm': 'millimetre',
    'yd': 'yard',
    '"': 'inch',},


    # Weight Units
    'item_weight':{'g': 'gram',
    'kg': 'kilogram',
    'mcg': 'microgram',
    'mg': 'milligram',
    'oz': 'ounce',
    'lb': 'pound',
    't': 'ton',}, 

    'maximum_weight_recommendation':{'g': 'gram',
    'kg': 'kilogram',
    'mcg': 'microgram',
    'mg': 'milligram',
    'oz': 'ounce',
    'lb': 'pound',
    't': 'ton',},


    'voltage':{
    'kv': 'kilovolt',
    'mv': 'millivolt',
    'v': 'volt'},

    # Power Units
    "wattage":{
    'kw': 'kilowatt',
    'w': 'watt'},

    # Volume Units
    "item_volume":{
    'cl': 'centilitre',
    'cf': 'cubic foot',
    'ci': 'cubic inch',
    'cup': 'cup',  # no abbreviation
    'dl': 'decilitre',
    'fl oz': 'fluid ounce',
    'gal': 'gallon',
    'imp gal': 'imperial gallon',
    'l': 'litre',
    'ml': 'millilitre',
    'ul': 'microlitre',
    'pt': 'pint',
    'qt': 'quart'
    }
}

allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}
allowed_abv_units = {unit for entity in unit_abbreviation_map for unit in unit_abbreviation_map[entity]}