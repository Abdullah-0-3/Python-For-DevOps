# Image Editor

import os
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def process_images(path, path_out):
    for filename in os.listdir(path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(path, filename))
            img = img.convert("RGB")
            img = img.filter(ImageFilter.SHARPEN)
            img = ImageEnhance.Color(img).enhance(1)
            img = ImageEnhance.Brightness(img).enhance(1)
            img = ImageEnhance.Contrast(img).enhance(1.2)
            img = img.filter(ImageFilter.GaussianBlur(radius=1))
            img = ImageOps.autocontrast(img)
            img.save(os.path.join(path_out, filename), "JPEG")

def enhance_images():
    path = "./images/"
    path_out = "./edited_images/"

    create_directory(path_out)
    process_images(path, path_out)
    
    print("All images have been edited and saved in the 'edited_images' folder.")

if __name__ == "__main__":
    enhance_images()