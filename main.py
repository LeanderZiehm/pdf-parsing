from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from pdf_libs import pdfplumber_module, pypdf_module, pymupdf_module, pdfminer_module

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

PDF_DIR = "static/pdfs"


@app.get("/", response_class=HTMLResponse)
def list_pdfs(request: Request):
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]
    return templates.TemplateResponse("index.html", {"request": request, "pdfs": pdf_files})


@app.get("/compare/{filename}", response_class=HTMLResponse)
def compare_pdf(request: Request, filename: str):
    pdf_path = os.path.join(PDF_DIR, filename)

    results = {
        "pdfplumber": pdfplumber_module.extract_text(pdf_path),
        "pypdf": pypdf_module.extract_text(pdf_path),
        "pymupdf": pymupdf_module.extract_text(pdf_path),
        "pdfminer": pdfminer_module.extract_text(pdf_path),
    }

    return templates.TemplateResponse(
        "compare.html",
        {"request": request, "filename": filename, "results": results},
    )
