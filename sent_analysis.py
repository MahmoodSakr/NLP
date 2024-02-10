import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK resources
nltk.download('vader_lexicon')

# Create a Sentiment Intensity Analyzer
sid = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
# text = "This movie is really good! I enjoyed every moment of it."
# text = "This movie is really bad! I didnt enjoyed every moment of it."
text = "This movie is neutral ! I didnt able to detect its nature."

# Perform sentiment analysis
scores = sid.polarity_scores(text)

print(f"scores['compound'] {scores['compound']}")

# Interpret the sentiment scores
if scores['compound'] >= 0.05:
    print("Positive")
elif scores['compound'] <= -0.05:
    print("Negative")
else:
    print("Neutral")
