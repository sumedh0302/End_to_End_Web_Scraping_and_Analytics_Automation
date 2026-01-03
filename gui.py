import tkinter as tk
from tkinter import messagebox
import subprocess
import json

def run_scraper():
    subprocess.run(["python", "scraper.py"])
    messagebox.showinfo("Done", "Scraping completed")

def run_analysis():
    subprocess.run(["python", "data_analysis.py"])
    messagebox.showinfo("Done", "Data analysis completed")

def launch_dashboard():
    subprocess.run(["python", "-m", "streamlit", "run", "dashboard.py"])

root = tk.Tk()
root.title("Web Scraping Automation")

tk.Button(root, text="Run Scraper", command=run_scraper, width=30).pack(pady=10)
tk.Button(root, text="Run Analysis", command=run_analysis, width=30).pack(pady=10)
tk.Button(root, text="Launch Dashboard", command=launch_dashboard, width=30).pack(pady=10)

root.mainloop()
