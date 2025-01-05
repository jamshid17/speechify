from pydantic import BaseModel

class OCRResponse(BaseModel):
    extracted_text: str
    
class TextToSpeechRequest(BaseModel):
    text: str