from PyPDF2 import PdfReader, PdfWriter, PdfFileWriter
from PyPDF2.generic import AnnotationBuilder

# Fill the writer with the pages you want
# pdf_path = os.path.join(RESOURCE_ROOT, "adasd.pdf")
reader = PdfReader("adasd.pdf")
page = reader.pages[0]
writer = PdfWriter()
writer.encrypt(user_password='', owner_pwd='sample_password', permissions_flag=0b0100)
writer.add_page(page)

# Create the annotation and add it
annotation = AnnotationBuilder.free_text(
    text="Hello World\nThis is the second line!",
    rect=(10, 10, 500, 40),
    font="Arial",
    bold=True,
    italic=True,
    font_size="10pt",
    border_color="000000",
    font_color="00FF00",
    background_color="FFFF00"
)
writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
with open("adasd_annotated.pdf", "wb") as fp:
    writer.write(fp)