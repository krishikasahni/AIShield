import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

def load_sms_dataset():
    """Load SMS Spam Collection dataset"""

    sms = pd.read_csv(
        RAW_DIR / "sms_spam.csv",
        encoding="latin-1",
        usecols=[0, 1]
    )

    sms.columns = ["label", "text"]

    sms["label"] = sms["label"].map({
        "ham": 0,
        "spam": 1
    })

    return sms


def load_youtube_dataset():
    """Load and merge all YouTube spam datasets"""

    files = [
        "Youtube01-Psy.csv",
        "Youtube02-KatyPerry.csv",
        "Youtube03-LMFAO.csv",
        "Youtube04-Eminem.csv",
        "Youtube05-Shakira.csv"
    ]

    dfs = []

    for file in files:
        df = pd.read_csv(RAW_DIR / file)

        df = df[["CONTENT", "CLASS"]]

        df.columns = ["text", "label"]

        dfs.append(df)

    youtube = pd.concat(dfs, ignore_index=True)

    return youtube


def load_all_data():

    sms = load_sms_dataset()

    youtube = load_youtube_dataset()

    data = pd.concat(
        [sms, youtube],
        ignore_index=True
    )

    return data