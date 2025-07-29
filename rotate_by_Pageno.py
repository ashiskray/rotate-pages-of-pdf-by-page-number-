#rotating pdf by page number 
import PyPDF2

#   first we will open file 
with open (r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\merge_pdf\merger_output.pdf","rb") as file :
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()
    rotate_pages=[1]    # just add page number [1,2,5,70] like this 
    for i, page in enumerate (reader.pages):
        if i in rotate_pages:
            page=page.rotate(90)
        writer.add_page(page)
with open ("rotatebypage.pdf","wb") as output_file:
    writer.write (output_file)