import PyPDF2
import sys

def add_wtm(pdf_list):
    wtm = PyPDF2.PdfFileReader(open('213_wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()

    for pdf in pdf_list:
        file = PyPDF2.PdfFileReader(open(pdf, 'rb'))
        num_of_pages = file.getNumPages()
        for p in range(num_of_pages):
            page = file.getPage(p)
            page.mergePage(wtm.getPage(0))
            output.addPage(page)
            output.write(open('drafted.pdf', 'wb'))

inputs = sys.argv[1:]
add_wtm(inputs)                 
