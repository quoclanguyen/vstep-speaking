from fastapi import FastAPI, UploadFile, File, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.process import *
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "filename": None})

@app.post("/upload", response_class=HTMLResponse)
async def upload_wav(request: Request, file: UploadFile = File(...), question: str = Form()):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    transc = transcribeAudio(file_location)
    result = assessTranscript_G(question = question, transcript = transc, json_result = assessPronunciation(file_location, transc))
    print(result)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "filename": file.filename,
        "result": result
    })
