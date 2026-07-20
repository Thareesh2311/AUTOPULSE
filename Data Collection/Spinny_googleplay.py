import pandas as pd
from google_play_scraper import reviews, Sort

APP_ID = "com.spinny.consumer"

all_reviews = []
continuation_token = None
MAX_REVIEWS = 50000

print("Downloading reviews...\n")

while len(all_reviews) < MAX_REVIEWS:

    result, continuation_token = reviews(
        APP_ID,
        lang="en",
        country="in",
        sort=Sort.NEWEST,
        count=200,  
        continuation_token=continuation_token
    )

    if not result:
        print("No more reviews found.")
        break

    for r in result:

        review_text = r.get("content", "").strip()

        if review_text == "":
            continue

        all_reviews.append({
            "platform": "Spinny",
            "review": review_text,
            "rating": r.get("score", ""),
            "date": r["at"].strftime("%Y-%m-%d"),
            "source": "Google Play"
        })

    print(f"Collected {len(all_reviews)} reviews...")

    if continuation_token is None:
        break


df = pd.DataFrame(all_reviews)

if not df.empty:
    df.drop_duplicates(subset=["review"], inplace=True)

filename = "spinny_google_play_reviews.csv"

df.to_csv(
    filename,
    index=False,
    encoding="utf-8-sig"
)


print("Download Complete!")
print(f"Total Reviews: {len(df)}")
print(f"Saved as: {filename}")

print("\nPreview:")
print(df.head())