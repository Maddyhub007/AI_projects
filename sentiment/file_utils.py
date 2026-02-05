import pandas as pd
import pdfplumber

def read_csv(file):
    df = pd.read_csv(file)
    return df.iloc[:, 0].dropna().tolist()  # assumes reviews in first column

def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    # Split into lines (each line = review)
    return [line.strip() for line in text.split("\n") if line.strip()]