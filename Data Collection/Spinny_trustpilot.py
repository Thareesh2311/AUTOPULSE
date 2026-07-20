import os
import time
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

DOMAIN = "spinny.com"
PLATFORM = "Spinny"


options = Options()


options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 20)

all_reviews = []

page = 1

while True:

    url = f"https://www.trustpilot.com/review/{DOMAIN}?page={page}"

    print(f"\nScraping Page {page}")

    driver.get(url)

    try:
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
    except:
        print("No review cards found.")
        break

    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    cards = soup.find_all("article")

    print("Cards Found:", len(cards))

    if len(cards) == 0:
        break

    previous_count = len(all_reviews)

    for card in cards:

        rating = ""
        title = ""
        review = ""
        date = ""


        img = card.find("img")

        if img:

            alt = img.get("alt", "")

            if "Rated" in alt:
                try:
                    rating = int(alt.split()[1])
                except:
                    pass

        time_tag = card.find("time")

        if time_tag:
            date = time_tag.get("datetime", "")


        h2 = card.find("h2")

        if h2:
            title = h2.get_text(strip=True)


        paragraphs = card.find_all("p")

        longest = ""

        for p in paragraphs:

            txt = p.get_text(" ", strip=True)

            if len(txt) > len(longest):
                longest = txt

        review = longest

        if review != "":

            all_reviews.append({
                "platform": PLATFORM,
                "title": title,
                "review": review,
                "rating": rating,
                "date": date,
                "source": "Trustpilot"
            })

    print(f"Collected {len(all_reviews)} reviews")

    if len(all_reviews) == previous_count:
        print("No new reviews found. Stopping...")
        break

    page += 1

driver.quit()


df = pd.DataFrame(all_reviews)

if not df.empty:
    df.drop_duplicates(subset=["review"], inplace=True)

filename = "spinny_trustpilot_reviews.csv"

df.to_csv(
    filename,
    index=False,
    encoding="utf-8-sig"
)

print("Scraping Completed")
print(f"Total Reviews : {len(df)}")

print(df.head())