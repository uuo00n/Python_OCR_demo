import pytesseract as pt
from PIL import Image

path = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

pt.pytesseract.tesseract_cmd = path

img = Image.open("pic/test_Chinese&English.png")

text = pt.image_to_string(img,lang="chi_sim")

print(text);