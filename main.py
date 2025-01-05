from fastapi import FastAPI
from routers import ocr_router, tts_router

app = FastAPI()

app.include_router(ocr_router.router, prefix="/ocr", tags=["OCR"])
app.include_router(tts_router.router, prefix="/tts", tags=["TTS"])

@app.get("/")
def root():
    return {"message": "Welcome to the Text-to-Speech and OCR API"}