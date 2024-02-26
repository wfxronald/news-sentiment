#import nltk
#nltk.download("all", quiet=True)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


analyzer = SentimentIntensityAnalyzer()


def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text


def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores["compound"]


def analyze_sentiments(snippets):
    result = []
    for snippet in snippets:
        result.append({
            "text": snippet,
            "sentiment": get_sentiment(preprocess_text(snippet)),
        })
    return result
