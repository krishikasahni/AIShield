from data_loader import load_all_data
from preprocess import clean_text

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

import joblib
from pathlib import Path

# -----------------------------
# Load data
# -----------------------------

df = load_all_data()

print(f"Dataset Size: {len(df)}")

# -----------------------------
# Clean text
# -----------------------------

print("Cleaning text...")

df["clean_text"] = df["text"].apply(clean_text)

# -----------------------------
# Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    df["clean_text"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"],
)

# -----------------------------
# TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2)
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# -----------------------------
# Model
# -----------------------------

model = LogisticRegression(max_iter=1000)

print("Training model...")

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------

predictions = model.predict(X_test)

print("\nAccuracy")

print(accuracy_score(y_test, predictions))

print("\nClassification Report")

print(classification_report(y_test, predictions))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, predictions))

# -----------------------------
# Save
# -----------------------------

SAVE_DIR = Path("ml/saved_models")
SAVE_DIR.mkdir(parents=True, exist_ok=True)

joblib.dump(model, SAVE_DIR / "spam_model.pkl")
joblib.dump(vectorizer, SAVE_DIR / "vectorizer.pkl")

print("\nModel Saved Successfully!")