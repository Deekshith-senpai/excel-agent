from fastapi import FastAPI, UploadFile, File
from app.parser import parse_excel

app = FastAPI(title="LatSpace Excel AI Parser")


@app.post("/parse")
async def parse(file: UploadFile = File(...)):
    return await parse_excel(file)