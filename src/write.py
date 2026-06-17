def print_reviews_by_id(all_reviews, matching_review_ids, path):
    
    if not matching_review_ids:
        with open(path, "w", encoding="utf-8") as file:
            file.write("No reviews found.\n")
        return

    with open(path, "w", encoding="utf-8") as file:
        for row in all_reviews:
            if row["review_id"] in matching_review_ids:
                file.write(str(row["review_id"]) + "\n")
                file.write(row["review_text"] + "\n\n")