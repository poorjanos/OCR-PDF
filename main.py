# https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


# We may need to do some additional downloading and setup...
# Windows needs a PyTesseract Download
# https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine
pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Users\poorj\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    )
 
# Windows also needs poppler_exe
# https://github.com/oschwartz10612/poppler-windows/issues/42
path_to_poppler_exe = Path(r"C:\Users\poorj\Projects\OCR-PDF\poppler-24.02.0\Library\bin")
     
# Put our output files in a sane place...
out_directory = Path(r"C:\Users\poorj\Projects\OCR-PDF\output")

# Path of the Input pdf
PDF_file = Path(r"C:\Users\poorj\Projects\OCR-PDF\input\karviraj.pdf")

#Path to Temp folder
temp_directory = Path(r"C:\Users\poorj\Projects\OCR-PDF\temp")
 
# Store all the pages of the PDF in a variable
image_file_list = [] 
text_file = out_directory / Path("out_text.txt")


# Part #1 : Converting PDF to images
pdf_pages = convert_from_path(
                PDF_file, 500, poppler_path=path_to_poppler_exe
            )

for page_enumeration, page in enumerate(pdf_pages, start=1):
    filename = f"page_{page_enumeration}.jpg"
    page.save(temp_directory / filename, "JPEG")
    image_file_list.append(filename)

with open(text_file, "a", encoding='utf-8') as output_file:
    for image_file in image_file_list:
        text = str(((pytesseract.image_to_string(Image.open(temp_directory / image_file), lang='hun'))))
        text = text.replace("-\n", "")
        output_file.write(text)