import streamlit as st
import pandas as pd
from sentiment import analyze_sentiment
from file_utils import read_csv, read_pdf

st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

st.title("📊 Review Sentiment Analyzer")
st.write("Upload a PDF or CSV file containing reviews")

uploaded_file = st.file_uploader(
    "Upload file", type=["pdf", "csv"]
)

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        reviews = read_csv(uploaded_file)
    else:
        reviews = read_pdf(uploaded_file)

    st.success(f"Loaded {len(reviews)} reviews")

    if st.button("Analyze Sentiment"):
        results = []
        progress = st.progress(0)

        for i, review in enumerate(reviews):
            sentiment = analyze_sentiment(review)
            results.append({
                "Review": review,
                "Sentiment": sentiment
            })
            progress.progress((i + 1) / len(reviews))

        df = pd.DataFrame(results)

        st.subheader("🔍 Sentiment Results")
        st.dataframe(df)

        # Overall sentiment
        sentiment_counts = df["Sentiment"].value_counts()

        st.subheader("📈 Overall Sentiment Distribution")
        st.bar_chart(sentiment_counts)

        st.download_button(
            "📥 Download Results as CSV",
            df.to_csv(index=False),
            file_name="sentiment_results.csv",
            mime="text/csv"
        )