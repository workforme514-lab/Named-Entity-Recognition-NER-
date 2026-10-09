
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import spacy

app = FastAPI(
    title="Named Entity Recognition API",
    description="API for extracting named entities from text",
    version="1.0.0",
)

# Load the pre-trained English NLP model
nlp = spacy.load("en_core_web_sm")


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="Text to analyze",
    )


@app.get("/")
def home():
    return {
        "message": "NER API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(request: TextRequest):
    text = request.text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Please enter some text.",
        )

    doc = nlp(text)

    entities = [
        {
            "text": entity.text,
            "label": entity.label_,
            "description": spacy.explain(entity.label_) or entity.label_,
            "start": entity.start_char,
            "end": entity.end_char,
        }
        for entity in doc.ents
    ]

    return {
        "input_text": text,
        "entity_count": len(entities),
        "entities": entities,
    }