import easyocr
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter

def read_text_from_image(image_path):
    reader = easyocr.Reader(['en'])  # Initialize the reader
    result = reader.readtext(image_path, detail=0)  # Read text from the image
    # print(type(result))
    return result

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

# save a sharpened, greyscale version of the image
def sharpen_greyscale(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale
    image = image.filter(ImageFilter.SHARPEN)  # Apply sharpening filter

    #Save modified image
    image.save(r"{image_path}-processed.jpg")


def main():
    # image_path="hello"
    # print(r"{image_path}-processed")
    print("Please select an image file for OCR processing.")
    sharpen_greyscale(get_image_path())
    local_image_path = get_image_path()
    result = read_text_from_image(local_image_path)
    print(result)

if __name__ == "__main__":
    main()