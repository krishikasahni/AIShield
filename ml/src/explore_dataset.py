import pandas as pd

sms = pd.read_csv(
    "ml/data/raw/sms_spam.csv",
    encoding="latin-1",
    usecols=[0, 1]
)

sms.columns = ["label", "text"]

print("\nFirst 5 rows:")
print(sms.head())

print("\nShape:")
print(sms.shape)

print("\nColumns:")
print(sms.columns)

print("\nClass Distribution:")
print(sms["label"].value_counts())