from PIL import Image
import pytesseract


#80 1000
#50 650 1270 1880

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
 
    text = pytesseract.image_to_string(Image.open(filename), lang="rus")  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


print(ocr_core('images/ocr_example_2.png'))