from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.predict import predict_comment
from backend.schemas import CommentRequest
app = FastAPI(title="AIShield API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AIShield Backend Running"
    }


@app.post("/predict")
def predict(request: CommentRequest):

    return predict_comment(request.text)