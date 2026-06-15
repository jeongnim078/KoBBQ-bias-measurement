from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_sentiment(text):

    result = classifier(text)[0]

    return result["label"]