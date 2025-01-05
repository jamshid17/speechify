# Text-to-Speech and OCR Backend

## Overview
This is a Python-based backend project for converting images to text using Optical Character Recognition (OCR) and text-to-speech (TTS) functionalities. It uses FastAPI for API routing and provides modular components for scalability and maintainability.

## Features
- Extract text from images using Tesseract OCR.
- Convert extracted text to speech with support for saving audio files.
- Modular architecture for easy extension.

## Project Structure
```
project/
├── main.py                 # Entry point for the FastAPI application
├── routers/                # Contains API routes
│   ├── __init__.py
│   ├── ocr_router.py
│   └── tts_router.py
├── schema/                 # Defines request and response schemas
│   ├── __init__.py
│   └── base_schema.py
├── service/                # Handles core logic for OCR and TTS
│   ├── __init__.py
│   └── base_service.py
├── models/                 # Database models using SQLAlchemy
│   ├── __init__.py
│   └── base_model.py
├── backend/                # Database connection setup
│   ├── __init__.py
│   ├── database.py
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── pyproject.toml          # Project dependencies managed by Poetry
└── README.md               # Project documentation
```

## Requirements
- Python 3.8+
- Dependencies listed in `pyproject.toml`:
  - FastAPI
  - pyttsx3
  - pytesseract
  - SQLAlchemy
  - Uvicorn
  - python-multipart
  - python-dotenv
  - gTTS

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/text-to-speech-ocr.git
cd text-to-speech-ocr
```

### 2. Install Dependencies
Use Poetry to install dependencies:
```bash
pip install poetry
poetry install
```

### 3. Set Up Environment Variables
Create a `.env` file and add your database URL:
```
DATABASE_URL=sqlite:///./test.db
```

### 4. Run the Application
Use Uvicorn to start the FastAPI server:
```bash
poetry run uvicorn main:app --reload
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints
### Root
- `GET /` - Welcome message.

### OCR
- `POST /ocr/extract-text/`
  - Accepts: Image file (multipart/form-data).
  - Returns: Extracted text from the image.

### Text-to-Speech
- `POST /tts/convert/`
  - Accepts: Text (JSON payload).
  - Returns: Success message and optionally the audio file.

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For questions or collaboration, reach out to [Your Name](mailto:your.email@example.com).
