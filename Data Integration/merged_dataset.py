import os
import pandas as pd

files = [
    "cars24_google_play_reviews.csv",
    "cars24_trustpilot.csv",
    "spinny_google_play_reviews.csv",
    "spinny_trustpilot_reviews.csv"
]

dfs = []

print("Reading CSV files...\n")

for file in files:

    if not os.path.exists(file):
        print(f"{file} not found")
        continue

    df = pd.read_csv(file)

    print(f"Reading {file}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print("-" * 50)

    # Keep only required columns
    required = [
        "platform",
        "review",
        "rating",
        "date",
        "source"
    ]

    df = df[[c for c in required if c in df.columns]]

    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

print("\nTotal Reviews Before Removing Duplicates:", len(merged_df))

merged_df.drop_duplicates(subset=["review"], inplace=True)

merged_df.reset_index(drop=True, inplace=True)

print("Total Reviews After Removing Duplicates:", len(merged_df))

merged_df.to_csv(
    "final_reviews_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nDataset Merged Successfully!")

print(os.path.abspath("final_reviews_dataset.csv"))