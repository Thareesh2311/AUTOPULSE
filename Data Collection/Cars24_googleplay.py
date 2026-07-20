import pandas as pd
from google_play_scraper import reviews_all

print("Downloading reviews...")

reviews = reviews_all(
    "com.cars24.seller",
    lang="en",
    country="in"
)

print("Downloaded:", len(reviews))

rows = []

df = pd.DataFrame(rows)


df.drop_duplicates(subset=["review"], inplace=True)

df.to_csv(
    "spinny_google_play_reviews.csv",
    index=False,
    encoding="utf-8-sig"
)

print("CSV saved successfully!")


for r in reviews:
    text = r.get("content", "").strip()

    # Skip empty ratings without review text
    if not text:
        continue

    rows.append({
        "platform": "Cars24",
        "review": text,
        "rating": r.get("score"),
        "date": r["at"].strftime("%Y-%m-%d"),
        "source": "Google Play"
    })

df = pd.DataFrame(rows)

df.drop_duplicates(subset=["review"], inplace=True)

df.to_csv(
    "cars24_google_play_reviews.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())
print("Saved", len(df), "reviews.")