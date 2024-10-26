from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List
from src.main import translate_text

app = FastAPI(title="English-to-Nigerian Translation API", version="1.0")

MODEL_NAME = "model"

# Supported languages
SUPPORTED_LANGUAGES = ["ig", "yo", "ha"]


class TranslationRequest(BaseModel):
    text: str = Field(..., example="""Experienced Senior Machine
                       Learning Engineer with a 
                      focus on MLOps, Cloud Infrastructure, 
                      and Deep Learning. Expertise in speech, 
                      text, and vision models.""") 
    
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

@app.get("/", response_model=dict)
async def root():
    return {"message": "Welcome to the English-to-Nigerian Translation API! Use the /translate/ endpoint to get started."}