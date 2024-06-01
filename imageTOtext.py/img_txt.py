import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\alist\AppData\Local\Programs\Tesseract-OCR\tesseract'
from PIL import Image

# Path to the image file
image_path = 'imageTOtext.py/image00198.jpeg'

# Open the image file
img = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = tess.image_to_string(img)

# Print the extracted text
print(text)
