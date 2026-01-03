import json
import os
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

HEADERS = {"User-Agent": "Mozilla/5.0"}
CHROMEDRIVER_PATH = "C:/path/to/chromedriver.exe"  # <-- update path

def scrape_site(site):
    print(f"Scraping: {site['name']} - {site['url']}")
    data = []

    # Dynamic site (Selenium)
    if site.get("dynamic"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
        driver.get(site["url"])
        time.sleep(5)  

        containers = driver.find_elements(By.CSS_SELECTOR, site["container"])
        for c in containers:
            row = {"Website": site["name"]}
            for field, selector in site["fields"].items():
                try:
                    el = c.find_element(By.CSS_SELECTOR, selector)
                    row[field] = el.text.strip()
                except:
                    row[field] = ""
            data.append(row)
        driver.quit()

    # Static site (Requests + BeautifulSoup)
    else:
        response = requests.get(site["url"], headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        containers = soup.select(site["container"])
        for c in containers:
            row = {"Website": site["name"]}
            for field, selector in site["fields"].items():
                el = c.select_one(selector)
                row[field] = el.text.strip() if el else ""
            data.append(row)

    return data

def scrape_all():
    with open("config.json", "r", encoding="utf-8") as f:
        websites = json.load(f)

    all_data = []
    for site in websites:
        try:
            all_data.extend(scrape_site(site))
        except Exception as e:
            print(f" Failed {site['name']}: {e}")

    if not all_data:
        print(" No data scraped")
        return

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(all_data)
    df.to_csv("data/raw_data.csv", index=False)
    print(f" Scraped {len(df)} total records")

if __name__ == "__main__":
    scrape_all()
