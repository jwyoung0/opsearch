from db import load_reviews, print_reviews_by_id    
from indexing import build_postings_list
from search.boolean import boolean_search


def main():
    reviews = load_reviews()

    postings = build_postings_list(reviews)

    query1 = ["happy", "phone"]

    matching_review_ids = boolean_search(postings, query1)
    
    print_reviews_by_id(matching_review_ids)



if __name__ == "__main__":
    main()