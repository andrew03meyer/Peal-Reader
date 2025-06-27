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

# ocr = paddleocr.OCR(lang='en')
ocr = PaddleOCR(lang="en")
result = ocr.predict("C:/Files/Peal Reader/media/test.png")

print("OCR Result: ", result.__len__(), " results found.")
for res in result:
    res.print()
    # res.save_to_img("output")
    # res.save_to_json("output")

    