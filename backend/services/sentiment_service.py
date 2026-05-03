import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

# Ensure nltk data is downloaded to a path accessible by the app
nltk_data_dir = os.path.join(os.path.dirname(__file__), "..", "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)
nltk.download('vader_lexicon', download_dir=nltk_data_dir, quiet=True)

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    
    if score > 0.05:
        return "Positive", score
    elif score < -0.05:
        return "Negative", score
    else:
        return "Neutral", score