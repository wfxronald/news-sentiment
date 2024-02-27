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


# this method mutates the existing data dictionary
def analyze_sentiments(results):
    for result in results:
        text = result["text"]
        overall_sentiment = get_sentiment(preprocess_text(text))
        result["sentiment"] = overall_sentiment

        # assume split by lines
        lines_of_text = text.splitlines()
        lines_with_sentiment = []
        for line in lines_of_text:
            lines_with_sentiment.append((line, get_sentiment(preprocess_text(line))))
        lines_with_sentiment.sort(key=lambda tup: abs(tup[1]), reverse=True)
        result["lines_with_sentiment"] = lines_with_sentiment[0:3]
