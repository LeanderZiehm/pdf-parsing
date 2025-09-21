from fastapi import FastAPI
from pdf_libs import pdfplumber_module, pypdf_module, pymupdf_module, pdfminer_module

app = FastAPI()

PDF_FILE = "pdfs/form_1786.pdf"

@app.get("/pdfplumber")
def read_with_pdfplumber():
    return {"text": pdfplumber_module.extract_text(PDF_FILE)}

@app.get("/pypdf")
def read_with_pypdf():
    return {"text": pypdf_module.extract_text(PDF_FILE)}

@app.get("/pymupdf")
def read_with_pymupdf():
    return {"text": pymupdf_module.extract_text(PDF_FILE)}

@app.get("/pdfminer")
def read_with_pdfminer():
    return {"text": pdfminer_module.extract_text(PDF_FILE)}