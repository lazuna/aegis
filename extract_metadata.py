import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        image = Image.open(file_path)
        info = image._getexif()
        if info:
            return {TAGS.get(tag): value for tag, value in info.items()}
    return None

file_path = 'image.jpg'
metadata = extract_metadata(file_path)
if metadata:
    print(f"Metadata for {file_path}: {metadata}")
else:
    print("No metadata found.")
