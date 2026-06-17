import os

import mysql.connector
from dotenv import load_dotenv


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

def boolean_search_and(postings, word1, word2):
    ### Conjunctive Boolean Search

    postings1 = postings.get(word1, [])
    postings2 = postings.get(word2, [])

    index1 = 0
    index2 = 0

    result = []

    while index1 < len(postings1) and index2 < len(postings2):
        if postings1[index1] == postings2[index2]:
            result.append(postings1[index1])
            index1 += 1
            index2 += 1    
        elif postings1[index1] < postings2[index2]:
            index1 += 1
        else: 
            index2 += 1  

    return result

def print_reviews_by_id(cursor, review_ids):
    if review_ids:
        placeholders = ", ".join(["%s"] * len(review_ids))

        cursor.execute(f"""
            SELECT review_id, review_text
            FROM reviews_segment
            WHERE review_id IN ({placeholders})
        """, review_ids)

        for row in cursor.fetchall():
            print(row["review_id"])
            print(row["review_text"])
            print()
    else:
        print("No reviews found.")

def main():

    load_dotenv()

    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )

    cursor = connection.cursor(dictionary=True)


    # LIMIT is for development stage. Should be removed for full run.
    cursor.execute("""
        SELECT review_id, review_text
        FROM reviews_segment
        ORDER BY review_id
        LIMIT 5000                   
    """)

    rows = cursor.fetchall()
    postings = build_postings_list(rows)

    matching_review_ids = boolean_search_and(postings, "happy", "phone")
    
    print_reviews_by_id(cursor, matching_review_ids)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()