from db import load_reviews  
from indexing import build_postings_list
from write import print_reviews_by_id
from search.boolean import boolean_search



def main():
    reviews = load_reviews()

    postings = build_postings_list(reviews)

    query1 = ["happy", "phone"]

    matching_review_ids = boolean_search(postings, query1)
    
    path = "src\\search\\boolean_results.txt"
    print_reviews_by_id(reviews, matching_review_ids, path)



if __name__ == "__main__":
    main()