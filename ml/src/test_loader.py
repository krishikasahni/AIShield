from data_loader import load_all_data

df = load_all_data()

print(df.head())

print()

print(df.shape)

print()

print(df["label"].value_counts())