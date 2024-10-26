from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List

# Import the existing translation function
from src.main import translate_text  # Replace with the actual file name

# Define the FastAPI app
app = FastAPI(title="English-to-Nigerian Translation API", version="1.0")

# Define the model name for the Hugging Face model
MODEL_NAME = "HelpMumHQ/AI-translator-eng-to-9ja"

# Supported languages
SUPPORTED_LANGUAGES = ["ig", "yo", "ha"]

# Define request body model using Pydantic
class TranslationRequest(BaseModel):
    text: str = Field(..., example="Healthcare is important.")  # Example text
    source_lang: str = Field("en", example="en", description="Source language code (default: 'en')")
    target_lang: str = Field(..., example="yo", description="Target language code (e.g., 'ig', 'yo', 'ha')")

@app.post("/translate/", response_model=dict)
async def translate(request: TranslationRequest):
    # Validate target language
    if request.target_lang not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported target language: {request.target_lang}. Supported languages: {SUPPORTED_LANGUAGES}"
        )

    # Use the existing translate_text function
    try:
        translated_text = translate_text(
            model_name=MODEL_NAME,
            source_lang=request.source_lang,
            target_lang=request.target_lang,
            text=request.text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

    return {"translated_text": translated_text}

# @app.get("/translate/")
# async def translate_get(
#     text: str = Query(..., example="Healthcare is important."),
#     source_lang: str = Query("en", example="en", description="Source language code (default: 'en')"),
#     target_lang: str = Query(..., example="yo", description="Target language code (e.g., 'ig', 'yo', 'ha')")
# ):
#     # Validate target language
#     if target_lang not in SUPPORTED_LANGUAGES:
#         raise HTTPException(
#             status_code=400, 
#             detail=f"Unsupported target language: {target_lang}. Supported languages: {SUPPORTED_LANGUAGES}"
#         )

#     # Use the existing translate_text function from apis.py
#     try:
#         translated_text = translate_text(
#             model_name=MODEL_NAME,
#             source_lang=source_lang,
#             target_lang=target_lang,
#             text=text
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

#     return {"translated_text": translated_text}

@app.get("/", response_model=dict)
async def root():
    return {"message": "Welcome to the English-to-Nigerian Translation API! Use the /translate/ endpoint to get started."}