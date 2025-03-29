import fitz
import docx

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

# Function to extract text from a DOC file
def extract_text_from_doc(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to extract text from a document (PDF or DOCX)
def extract_text(file_path):
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx") or file_path.lower().endswith(".doc"):
        return extract_text_from_doc(file_path)
    else:
        raise ValueError("Unsupported file format. Only PDF, DOCX, and DOC are supported.")

