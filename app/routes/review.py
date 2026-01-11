from fastapi import APIRouter, UploadFile, File
from app.services.file_parser import extract_text
from app.services.ai_service import analyze_document

router = APIRouter()

@router.post("/review")
async def review_document(file: UploadFile = File(...)):
    text = extract_text(file)
    analysis = analyze_document(text)

    return {
        "filename": file.filename,
        "analysis": analysis
    }

