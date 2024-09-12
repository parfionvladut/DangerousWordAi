from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample data (for demonstration purposes)
data = [
    ('This is a dangerous message', 'high'),
    ('Just a regular message', 'low'),
    ('Warning: potential threat detected', 'high'),
    ('Hello, how are you?', 'low')
]

# Split data into training and testing
texts, labels = zip(*data)

# Create a pipeline with a vectorizer and a classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(texts, labels)

# Example function to classify new messages
def classify_threat(message):
    prediction = model.predict([message])
    return prediction[0]


