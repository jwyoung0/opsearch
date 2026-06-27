#Builds inverted index
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from preprocessing import build_stopwords_list

FREQUENCY_CUTOFF = 5

def build_postings_list(rows):
    """
    This is problematic because it does not properly strip words from punctuation
    that is why I went for the nltk route in the other function
    """
    
    postings = {}

    stopwords = build_stopwords_list()

    for row in rows:
        review_id = row["review_id"]
        review_text = row["review_text"]

        tokens = review_text.lower().split()

        for token in set(tokens):
            if token not in stopwords:
                if token not in postings:
                    postings[token] = []

                postings[token].append(review_id)    
 
    return postings

def build_postings_list2(rows):
    nltk.download("punkt_tab")
    nltk.download("stopwords")

    inverted_index = {}

    stop_words = set(stopwords.words("english"))

    for row in rows:
        review_id = row["review_id"]
        review_text = row["review_text"]

        tokens = word_tokenize(review_text.lower(), "english")

        for token in set(tokens):
            if token not in stop_words:
                inverted_index.setdefault(token, []).append(review_id)

    inverted_index = frequency_cutoff_index(inverted_index, FREQUENCY_CUTOFF)
    
    return inverted_index


def frequency_cutoff_index(index, cutoff):
    return {
        token: postings
        for token, postings in index.items()
        if len(postings) >= cutoff
    }

