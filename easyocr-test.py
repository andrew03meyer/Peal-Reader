import easyocr
import shutil
import tkinter as tk
from tkinter import filedialog

def read_text_from_image(image_path):
    reader = easyocr.Reader(['en'], gpu=False)  # Initialize the reader
    result = reader.readtext(image_path)  # Read text from the image
    for (bbox, text, confidence) in result:
        print(text)

def get_image_path():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    
    return file_path

def add_image_to_media():
    target_dir = "./media/"
    source_dir = get_image_path()

    try:
        shutil.copy(source_dir, target_dir)
    except FileNotFoundError:
        print(f"Error: The file {source_dir} does not exist.")

def main():
    print("Please select an image file for OCR processing.")
    local_image_path = get_image_path()
    read_text_from_image(local_image_path)

if __name__ == "__main__":
    main()