from db import load_reviews  
from indexing import build_postings_list
from output_writing import print_reviews_by_id
from search.boolean import boolean_opsearch
from pathlib import Path



def main():
    reviews = load_reviews()

    postings = build_postings_list(reviews)

    # for key in list(postings.keys())[:10]:
    #     print(key)
    #     print(postings[key])

    query1 = ["phone screen", "issues"]
    query2 = ["wifi signal", "weak"]
    query3 = ["mouse button", "great"]
    query4 = ["battery life", "long"]
    query5 = ["printer ink", "expensive"]

    query_list = (query1, query2, query3, query4, query5)

    for i, query in enumerate(query_list, start=1):
        matching_reviews = boolean_opsearch(postings, query)
        
        path = Path("outputs") / f"boolean_results{i}.txt"
        print_reviews_by_id(reviews, matching_reviews, path)



if __name__ == "__main__":
    main()