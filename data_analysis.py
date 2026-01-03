import pandas as pd
import os

def analyze():
    path = "data/raw_data.csv"
    if not os.path.exists(path):
        print("Run scraper first")
        return

    df = pd.read_csv(path)
    if df.empty:
        print("No data found")
        return

    df.drop_duplicates(inplace=True)
    df.to_csv("data/cleaned_data.csv", index=False)
    print("Analysis complete")

if __name__ == "__main__":
    analyze()
