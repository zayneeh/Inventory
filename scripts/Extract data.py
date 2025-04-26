from PyPDF2 import PdfReader
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os


def pdf_reader(file_path):
    try:
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
           text += page.extract_text()
        return text
    except Exception as e:
        print(f"PDF reader error: {e}")
        return None  

def ocr_reader(file_path):
    try:
        text = ''
        images = convert_from_path(file_path)
        for img in images:
            temp_path = "temp_image.png"
            img.save(temp_path, 'PNG')
            text += pytesseract.image_to_string(Image.open(temp_path))
            os.remove(temp_path)
        return text
    except Exception as e:
        print(f"OCR error: {e}")
        return None


def get_data_from_pdf(file_path):
    pdf_data = pdf_reader(file_path)
    if pdf_data:
        print(f"PDF read successfully")
        print(pdf_data)
    else:
        print("PDF reader failed. Triggering OCR fallback...")
        ocr_result = ocr_reader(pdf_data) 

