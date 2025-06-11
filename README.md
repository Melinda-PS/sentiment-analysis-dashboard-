📊 Sentiment Analysis Dashboard
An interactive web application that analyzes sentiment in user-provided text, customer reviews, or uploaded documents. Built using Streamlit, Hugging Face Transformers, and visualized with matplotlib and wordcloud.
https://curly-xylophone-v65g69qvrxgg266qw-8501.app.github.dev/



https://77c7-35-196-20-234.ngrok-free.app/

🔍Features
Text input or file upload (.txt or .csv)
Multi-class sentiment classification (Positive, Neutral, Negative)
Confidence scores for predictions
Keyword extraction for sentiment drivers
Batch processing of multiple texts
Visualizations: Sentiment distribution chart and WordCloud
Export results to CSV, JSON, and PDF
Explanation of sentiment predictions

🚀 Live Demo (Colab + ngrok)
To run this app from Google Colab and access it via a public link, you’ll need to use ngrok.

 🔐Ngrok Token
This app uses ngrok to create a public URL.
You need to set your token in the code. Get it from:
https://dashboard.ngrok.com/get-started/setup
In your Colab code, replace:
python
Copy
Edit
!ngrok authtoken YOUR_NGROK_TOKEN
with your actual token.

 Local Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/sentiment-analysis-dashboard.git
cd sentiment-analysis-dashboard
2. Install Dependencies
You can use pip:
bash
-Copy
-Edit
pip install -r requirements.txt

If you don’t have a requirements.txt, you can install manually:
bash
Copy
Edit
pip install streamlit transformers pandas matplotlib wordcloud fpdf pyngrok
4. Run the App
bash
Copy
Edit
streamlit run app.py
If using ngrok:

bash
Copy
Edit
python ngrok_starter.py
