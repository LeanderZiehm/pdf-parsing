from pdfrw import PdfReader

# ⚠️ pdfrw does not support text extraction directly,
# it's mainly for manipulation (merge, split, etc.)
# We'll extract raw content streams (not clean text).
def extract_text(file_path: str) -> str:
    pdf = PdfReader(file_path)
    text = ""
    for page in pdf.pages:
        if hasattr(page, "Contents") and page.Contents:
            streams = page.Contents.stream if hasattr(page.Contents, "stream") else ""
            text += str(streams)
    return text