import pdfkit
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import PyPDF2
import os

def create_pdf_with_colored_background(output_filename, background_color):
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4
    c.setFillColor(background_color)
    c.rect(0, 0, width + 10, height + 10, fill=1)
    c.showPage()
    c.setFillColor(background_color)
    c.rect(-2, -2, width + 4, height + 1, fill=1)
    c.showPage()
    c.save()

background_color = '#F1F1F1' 
create_pdf_with_colored_background("background.pdf", background_color)

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

options = {
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
}

pdfkit.from_file("index.html", "temp_result.pdf", configuration=config, options=options)

def merge_pdfs(pdf_with_background, pdf_from_html, output_pdf):
    with open(pdf_with_background, 'rb') as background_pdf_file, open(pdf_from_html, 'rb') as content_pdf_file:
        background_pdf = PyPDF2.PdfReader(background_pdf_file)
        content_pdf = PyPDF2.PdfReader(content_pdf_file)
        output_pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(background_pdf.pages)):
            page = background_pdf.pages[page_num]
            if page_num <= len(content_pdf.pages):
                page.merge_page(content_pdf.pages[page_num])
            output_pdf_writer.add_page(page)

        with open(output_pdf, 'wb') as output_file:
            output_pdf_writer.write(output_file)

merge_pdfs("background.pdf", "temp_result.pdf", "result.pdf")

os.remove("temp_result.pdf")
os.remove("background.pdf")
