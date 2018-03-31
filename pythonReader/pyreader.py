try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
from pathlib import Path
import os

# Set Tesseract Executable Path here
# Eg. 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
pathname = ''
filepath = Path(pathname).resolve()
pytesseract.pytesseract.tesseract_cmd = str(filepath)

# Set Image Path here
# Eg. 'C:\\Python\\reader\\TH02.png'
imgpath = ''
path_to_image = Path(imgpath).resolve()

# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open(str(path_to_image))))

# French text image to string
print(pytesseract.image_to_string(Image.open(str(path_to_image)), lang='tha')) # Set Lang here

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open(str(path_to_image))))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open(str(path_to_image))))