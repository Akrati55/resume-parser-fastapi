from fastapi import FastAPI
from fastapi.responses import JSONResponse
from resume_parser import parse_resume  # Import your resume parsing function

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Resume Parser API!"}

@app.post("/parse/")
async def parse(resume_file: UploadFile = File(...)):
    # Call your resume parsing logic here
    parsed_data = parse_resume(resume_file)
    return JSONResponse(content=parsed_data)

