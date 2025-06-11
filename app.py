import streamlit as st
from transformers import pipeline
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from fpdf import FPDF

st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

@st.cache_resource(show_spinner=True)
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

def extract_keywords(text, n=10):
    words = text.lower().split()
    freq = {}
    for w in words:
        if len(w) > 3 and w.isalpha():
            freq[w] = freq.get(w, 0) + 1
    keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [k for k, v in keywords[:n]]

def plot_sentiment_distribution(df):
    counts = df['label'].value_counts()
    fig, ax = plt.subplots()
    counts.plot(kind='bar', ax=ax, color=['green', 'orange', 'red'])
    ax.set_title("Sentiment Distribution")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of Texts")
    st.pyplot(fig)

def plot_wordcloud(keywords):
    text = " ".join(keywords)
    wc = WordCloud(width=400, height=200, background_color='white').generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

def export_results(df):
    st.markdown("### Export Results")

    # CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name='sentiment_results.csv')

    # JSON
    json_data = df.to_json(orient='records')
    st.download_button("Download JSON", data=json_data, file_name='sentiment_results.json')

    # PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sentiment Analysis Results", ln=True, align='C')

    for idx, row in df.iterrows():
        pdf.ln(5)
        pdf.cell(0, 10, txt=f"Text: {row['text'][:70]}...", ln=True)
        pdf.cell(0, 10, txt=f"Sentiment: {row['label']} (Confidence: {row['score']:.2f})", ln=True)
        pdf.cell(0, 10, txt=f"Keywords: {', '.join(row['keywords'])}", ln=True)

    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    st.download_button("Download PDF", data=pdf_bytes, file_name="sentiment_results.pdf")


def explain_sentiment(text, label):
    keywords = extract_keywords(text)
    reasons = ", ".join(keywords[:3])
    return f"This text was labeled **{label}** mainly due to keywords like: {reasons}"

def main():
    st.title("📊 Sentiment Analysis Dashboard")
    st.markdown("Analyze text sentiment using Hugging Face Transformers!")

    model = load_sentiment_model()

    st.markdown("## Enter text or upload a text file (.txt, .csv)")
    input_method = st.radio("Select input method", ("Text input", "File upload"))

    texts = []
    if input_method == "Text input":
        user_text = st.text_area("Enter text to analyze", height=150)
        if user_text:
            texts = [user_text]
    else:
        uploaded_file = st.file_uploader("Upload a .txt or .csv file", type=['txt', 'csv'])
        if uploaded_file:
            if uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                if 'text' in df.columns:
                    texts = df['text'].dropna().tolist()
                else:
                    st.error("CSV must contain a 'text' column.")
            else:
                file_text = uploaded_file.read().decode('utf-8').strip()
                texts = [line for line in file_text.split('\n') if line.strip()]

    if texts:
        st.markdown(f"### Analyzing {len(texts)} texts...")
        results = []
        for text in texts:
            try:
                output = model(text)[0]
                label = output['label']
                score = output['score']
                keywords = extract_keywords(text)
                explanation = explain_sentiment(text, label)
                results.append({
                    'text': text,
                    'label': label,
                    'score': score,
                    'keywords': keywords,
                    'explanation': explanation
                })
            except Exception as e:
                st.error(f"Error analyzing text: {e}")

        df_results = pd.DataFrame(results)
        st.dataframe(df_results[['text', 'label', 'score', 'keywords', 'explanation']])

        plot_sentiment_distribution(df_results)

        all_keywords = sum(df_results['keywords'].tolist(), [])
        st.markdown("### Keywords WordCloud")
        plot_wordcloud(all_keywords)

        export_results(df_results)

if __name__ == "__main__":
    main()
