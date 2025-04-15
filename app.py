from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import docx
import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

app = FastAPI()

class ResumeDetails(BaseModel):
    name: str
    email: str
    skills: list
    experience: str

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def parse_resume(resume_text):
    doc = nlp(resume_text)
    name = ""
    email = ""
    skills = ["Python", "Machine Learning", "NLP"]
    experience = ""

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
        elif ent.label_ == "EMAIL":
            email = ent.text
        elif ent.label_ == "ORG":
            experience = ent.text
    return ResumeDetails(name=name, email=email, skills=skills, experience=experience)

@app.post("/parse_resume/")
async def parse_resume_endpoint(file: UploadFile = File(...)):
    if file.filename.endswith(".docx"):
        text = extract_text_from_docx(file.file)
    elif file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    else:
        return {"error": "Unsupported file type"}
    resume_details = parse_resume(text)
    return resume_details
