from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from .resume_parser import parse_resume

app = FastAPI()

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    parsed_data = parse_resume(content)
    return JSONResponse(content=parsed_data)
