Sentiment Dashboard
Description:
Real-time sentiment analysis web app using Hugging Face and Streamlit.

Tech Stack:
Python, Streamlit, Hugging Face Transformers, matplotlib, wordcloud

Live Demo:
[Try it here](https://czk4haum5pvgxruigazj7r.streamlit.app/)📊

Sentiment Analysis Dashboard
An interactive web application that analyzes sentiment in user-provided text, customer reviews, or uploaded documents. Visualizes results with sentiment distribution charts and word clouds. Built with Streamlit, Hugging Face Transformers, matplotlib, and wordcloud.

🔍 Features
Input text or upload files (.txt or .csv)

Multi-class sentiment classification (Positive, Neutral, Negative)

Confidence scores for predictions

Keyword extraction highlighting sentiment drivers

Batch processing for multiple texts

Visualizations: sentiment distribution charts & WordClouds

Export results as CSV, JSON, or PDF

Explanation of sentiment predictions for transparency

🚀 Live Demo (Colab + Ngrok)
Run this app from Google Colab and access it publicly using ngrok.

🔐 Ngrok Token Setup
This app uses ngrok to create a public URL. You must set your token in the code.

Get your token from ngrok dashboard.

Replace in your Colab notebook:

python
Copy
Edit
!ngrok authtoken YOUR_NGROK_TOKEN
with your actual token.

🛠️ Local Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/sentiment-analysis-dashboard.git
cd sentiment-analysis-dashboard
Install dependencies:

If you have requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install streamlit transformers pandas matplotlib wordcloud fpdf pyngrok
Run the app:

bash
Copy
Edit
streamlit run app.py
If using ngrok:

bash
Copy
Edit
python ngrok_starter.py
