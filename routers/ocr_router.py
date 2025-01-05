from fastapi import APIRouter, UploadFile, File
from schema.base_schema import OCRResponse
from service.base_service import extract_text_from_image

router = APIRouter()

@router.post("/extract-text/", response_model=OCRResponse)
async def extract_text(file: UploadFile = File(...)):
    return await extract_text_from_image(file)