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

def print_text(local_image_path):
    # ocr = paddleocr.OCR(lang='en')
    ocr = PaddleOCR(lang="en")
    result = ocr.predict(local_image_path)

    print("OCR Result: ", result.__len__(), " results found.")
    for res in result:
        res.print()
        # res.save_to_img("output")
        # res.save_to_json("output")

def get_local_image_path():
    path = "./media/"
    file = ""

    print("Files in the directory:", path, "\n")
    print(os.listdir(path))
    
    while file not in os.listdir(path):
        file = input("Enter the image file name (e.g., test.png): ")
    
    full_path = os.path.join(path, file)
    return full_path

def add_image_to_media():
    target_dir = "./media/"
    source_dir = input("Enter the source directory path to copy the image from: ")
    image_name = input("Enter the image file name to copy: ")
    source_path = os.path.join(source_dir, image_name)
    try:
        shutil.copy(source_path, target_dir)
    except FileNotFoundError:
        print(f"Error: The file {source_path} does not exist.")

def main():
    print("Welcome to the PaddleOCR Test Script!")
    add_image = input("Do you want to add an image to the media folder? (yes/no): ").strip().lower()
    if add_image == 'yes':
        add_image_to_media()
        
    local_image_path = get_local_image_path()
    print_text(local_image_path)

if __name__ == "__main__":
    main()