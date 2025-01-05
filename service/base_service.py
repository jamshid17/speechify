import uuid 
from PIL import Image
from pathlib import Path
import pytesseract
import io
import pyttsx3
from gtts import gTTS
from fastapi.responses import JSONResponse

from schema.base_schema import OCRResponse


async def extract_text_from_image(file):
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        extracted_text = pytesseract.image_to_string(image)

        if not extracted_text.strip():
            return JSONResponse(content={"message": "No text detected."}, status_code=400)
        print(extracted_text)
        return OCRResponse(
            extracted_text=extracted_text
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
        
        
async def convert_text_to_speech(request):
    try:
        # Generate a unique file name
        output_dir = Path("audio_files")
        output_dir.mkdir(exist_ok=True)
        audio_file_path = output_dir / f"{uuid.uuid4()}.mp3"

        # Convert text to speech using gTTS
        tts = gTTS(text=request.text, lang='en')
        tts.save(str(audio_file_path))

        return {"message": "Text converted to speech successfully.", "audio_file": str(audio_file_path)}

    except Exception as e:
        return {"error": str(e)}