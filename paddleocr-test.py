# Intsall PaddleOCR if not already installed - python -m pip install paddlepaddle==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
# If fails to install:
    # Press Windows Key + R, type regedit, and press Enter to open the Registry Editor.
    # Navigate to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
    # Find an entry named LongPathsEnabled.
    # Double-click it and change its Value data from 0 to 1.
    # If LongPathsEnabled doesn't exist, right-click in the empty space, select New > DWORD (32-bit) Value, name it LongPathsEnabled, and then set its value to 1.
    # Restart your computer after making this change for it to take effect.
    # Try installing PaddleOCR again after the restart.
# I also had to run - pip install setuptools

from paddleocr import PaddleOCR
import os
import shutil
import tkinter as tk
from tkinter import filedialog

def print_text(local_image_path):
    # ocr = paddleocr.OCR(lang='en')
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False, 
        use_textline_orientation=False,
        lang="en",)
    
    result = ocr.predict(local_image_path)
    # result = ocr.ocr(local_image_path)

    # print("OCR Result: ", result.__len__(), " results found.")
    for res in result:
        res.print()
        # res.save_to_img("output")
        # res.save_to_json("output")

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
    # input("Press Enter to continue...")
    local_image_path = get_image_path()
    print_text(local_image_path)

if __name__ == "__main__":
    main()