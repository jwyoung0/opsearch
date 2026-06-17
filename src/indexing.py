def build_postings_list(rows):
    
    postings = {}

    for row in rows:
        review_id = row["review_id"]
        review_text = row["review_text"]

        tokens = review_text.lower().split()

        for token in set(tokens):
            if token not in postings:
                postings[token] = []

            postings[token].append(review_id)

    return postings