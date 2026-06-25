#Builds inverted index

from preprocessing import build_stopwords_list

def build_postings_list(rows):
    
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