import pandas as pd
from pathlib import Path

RAW_DATA = Path("ml/data/raw")

youtube_files = [
    "Youtube01-Psy.csv",
    "Youtube02-KatyPerry.csv",
    "Youtube03-LMFAO.csv",
    "Youtube04-Eminem.csv",
    "Youtube05-Shakira.csv"
]

youtube_data = []

print("=" * 50)
print("Loading YouTube datasets...")
print("=" * 50)

for file in youtube_files:
    df = pd.read_csv(RAW_DATA / file)

    print(f"{file} -> {df.shape}")

    youtube_data.append(df)

youtube = pd.concat(youtube_data, ignore_index=True)

print("\nCombined YouTube Dataset")
print(youtube.shape)

print("\nColumns:")
print(youtube.columns)

print("\nFirst 5 rows:")
print(youtube.head())