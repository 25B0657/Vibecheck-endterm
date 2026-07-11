import nltk
import re

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def preprocess(text):

    # Step 1: Convert to lowercase
    text = text.lower()

    # Step 2: Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Step 3: Tokenize
    tokens = word_tokenize(text)

    # Step 4: Remove stop words
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in tokens if word not in stop_words]

    # Step 5: Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    return lemmatized_words