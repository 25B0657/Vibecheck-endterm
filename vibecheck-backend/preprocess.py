import nltk
import pandas as pd
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#Question 2:

def preprocess(text):

    # step 1 is convert the text in lowercase
    text = text.lower()

    # step 2 is remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # step 3 is perform tokenization on the text
    tokens = word_tokenize(text)

    # step 4 is stop word removal from the english text
    stop_words = set(stopwords.words('english'))

    filtered_words = []

    for word in tokens:
        if word not in stop_words:
            filtered_words.append(word)

    # step 5 is perform lemmatization on the text
    lemmatizer = WordNetLemmatizer()

    lemmatized_words = []

    for word in filtered_words:
        lemmatized_words.append(lemmatizer.lemmatize(word))

    return lemmatized_words

