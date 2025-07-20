import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

# Set path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    return "\n".join(pytesseract.image_to_string(p) for p in pages)

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        return extract_text_from_image(file_path)
    elif ext == '.pdf':
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format")
    
if __name__ == "__main__":
    test_file = "data/receipt1.jpg" # or .pdf
    try:
        text = extract_text(test_file)
        print("✅ Text Extracted:\n")
        print(text)
    except Exception as e:
        print("❌ Error:", e)
   
    
