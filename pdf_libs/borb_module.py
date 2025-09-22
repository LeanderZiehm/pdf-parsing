from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction

def extract_text(file_path: str) -> str:
    with open(file_path, "rb") as pdf_file:
        doc = PDF.loads(pdf_file)
        if doc is None:
            return ""
        extractor = SimpleTextExtraction()
        doc.get_page(0).accept(extractor)
        return extractor.get_text()