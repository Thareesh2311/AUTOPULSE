import time
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



options = Options()


options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

all_reviews = []

MAX_PAGES = 5      

for page in range(1, MAX_PAGES + 1):

    print(f"Scraping page {page}...")

    url = f"https://www.trustpilot.com/review/cars24.com?page={page}"

    driver.get(url)

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
    except:
        print("No reviews found on page.")
        continue

    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    cards = soup.find_all("article")

    print("Cards Found:", len(cards))

    if len(cards) == 0:
        break

    for card in cards:

        review = ""
        rating = ""
        date = ""

        img = card.find("img")

        if img and img.get("alt"):
            alt = img["alt"]

            if "Rated" in alt:
                try:
                    rating = int(alt.split()[1])
                except:
                    rating = ""

        time_tag = card.find("time")

        if time_tag:
            date = time_tag.get("datetime", "")

      
        paragraphs = card.find_all("p")

        longest = ""

        for p in paragraphs:
            txt = p.get_text(strip=True)

            if len(txt) > len(longest):
                longest = txt

        review = longest

        if review != "":

            all_reviews.append(
                {
                    "platform": "Cars24",
                    "review": review,
                    "rating": rating,
                    "date": date,
                    "source": "Trustpilot"
                }
            )

driver.quit()

df = pd.DataFrame(all_reviews)

df.drop_duplicates(subset=["review"], inplace=True)

df.to_csv("cars24_trustpilot.csv", index=False, encoding="utf-8-sig")

print("\nFinished!")
print("Total Reviews:", len(df))
print(df.head())