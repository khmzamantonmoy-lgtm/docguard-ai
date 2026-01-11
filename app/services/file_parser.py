from PyPDF2 import PdfReader
import docx

def extract_text(file):
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        return " ".join([page.extract_text() for page in reader.pages])

    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        return " ".join([p.text for p in doc.paragraphs])

    elif file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    else:
        raise ValueError("Unsupported file format")

