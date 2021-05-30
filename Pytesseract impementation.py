try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


"""
This function will handle the core OCR processing of images.
"""
def ocr_core(filename):
    text=pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core("C:\DIA\DIA-PROJECT-INEURON\Salarysample.png"))



