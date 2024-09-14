import os
import requests
from tqdm import tqdm

def download_images_fixed(image_urls, save_dir):
    """
    Downloads images from a list of URLs and saves them to a specified directory.
    
    Args:
        image_urls (list): List of image URLs.
        save_dir (str): Directory to save the downloaded images.
    
    Returns:
        None
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for idx, url in tqdm(enumerate(image_urls),  total=len(image_urls)):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                # Set the image file name
                file_name = os.path.join(save_dir, f'image_{idx + 1}.jpg')
                
                # Write the image to the file
                with open(file_name, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                
                # print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")