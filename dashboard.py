import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("Multi-Website Web Scraping Dashboard")

if not os.path.exists("data/cleaned_data.csv"):
    st.error("Run scraper.py and data_analysis.py first")
else:
    df = pd.read_csv("data/cleaned_data.csv")
    st.subheader("Scraped Data")
    st.dataframe(df)

    st.subheader("Column Insights")
    for col in df.columns:
        st.write(f"### {col}")
        st.bar_chart(df[col].value_counts())
