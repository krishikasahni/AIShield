import joblib
from pathlib import Path

from ml.src.preprocess import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "ml" / "saved_models"

model = joblib.load(MODEL_DIR / "spam_model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")


def predict_comment(text):

    cleaned = clean_text(text)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0].max()

    return {
        "prediction": "Spam" if prediction == 1 else "Not Spam",
        "confidence": round(float(probability), 3),
    }