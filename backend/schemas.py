from pydantic import BaseModel


class CommentRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float