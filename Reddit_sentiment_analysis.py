from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Path to your uploaded file
file_path = '[file_path_excel]'

# Load the data
reddit_data = pd.read_excel(file_path)

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Extract content from the 'body' column
sentences = reddit_data['body'].dropna()

# Analyze sentiment and store scores
print("Sentiment Analysis Results:")
print("=" * 50)
for sentence in sentences:
    sentiment_score = analyzer.polarity_scores(sentence)
    print(f"Sentence: {sentence}")
    print(f"Positive: {sentiment_score['pos']}, Neutral: {sentiment_score['neu']}, Negative: {sentiment_score['neg']}, Compound:{sentiment_score['compound']}")
    print("-" * 50)


