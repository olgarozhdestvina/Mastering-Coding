import PyPDF2

with open('213_dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(180)
    with open('rotated_dummy.pdf', 'wb') as new_file:
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        writer.write(new_file)
