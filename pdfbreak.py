import PyPDF2
from pathlib import Path

input_pdf = Path(r"C:\Users\poorj\Projects\OCR-PDF\input\karviraj.pdf")
out_pdf = Path(r"C:\Users\poorj\Projects\OCR-PDF\output\kaviraj_short.pdf")

def extract_pages(input_pdf_path, output_pdf_path, pages):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(input_pdf_path)
    
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfFileWriter()
    
    # Extract the specified pages
    for page_num in pages:
        if page_num < pdf_reader.numPages:  # Check if the page number is within the range
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        else:
            print(f"Page number {page_num} is out of range. Skipping.")
    
    # Write the output PDF
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

extract_pages(input_pdf, out_pdf, pages=list(range(21, 41)))
