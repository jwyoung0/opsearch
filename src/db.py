import os

import mysql.connector
from dotenv import load_dotenv

def load_reviews():
    
    load_dotenv()

    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )

    cursor = connection.cursor(dictionary=True)


    query = """
        SELECT review_id, review_text
        FROM reviews_segment
        ORDER BY review_id
        LIMIT 5000
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return rows

def print_reviews_by_id(review_ids):
    if review_ids:
        placeholders = ", ".join(["%s"] * len(review_ids))

    load_dotenv()

    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )

    cursor = connection.cursor(dictionary=True)

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
    
    cursor.close()
    connection.close()
