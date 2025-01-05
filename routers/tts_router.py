from fastapi import APIRouter
from schema.base_schema import TextToSpeechRequest
from service.base_service import convert_text_to_speech

router = APIRouter()

@router.post("/convert/", status_code=200)
async def text_to_speech(request: TextToSpeechRequest):
    return await convert_text_to_speech(request)