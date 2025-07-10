from PIL import Image, ImageFilter
import pytesseract
import tkinter as tk
from tkinter import filedialog


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def get_image_path():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    
    return file_path

# image_path = get_image_path()
# image = Image.open(image_path)
# text = pytesseract.image_to_string(image)
# print("Extracted text:")
# print(text)

file_path = get_image_path()
# load the example image and convert it to grayscale
image = Image.open(file_path).filter(ImageFilter.SHARPEN)

# run tesseract, recognizing the handwritten text
text = pytesseract.image_to_string(image)

# print the recognized text
print(text)