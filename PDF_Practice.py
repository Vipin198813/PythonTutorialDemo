import PyPDF2
from PyPDF2 import PdfReader

f = open('Test-989.pdf','rb')
pdf_reader: PdfReader = PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))
page_one = pdf_reader.pages[0]
text = page_one.extract_text()
print(text)
f.close()

f = open('Test-989.pdf','rb')
PdfReader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page()
pdf_output = open('Some_New_Doc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()