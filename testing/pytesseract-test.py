from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image_path = r'C:\Files\Peal Reader\media\test4.jpg'

image = Image.open(image_path)
text = pytesseract.image_to_string(image)
print("Extracted text:")
print(text)