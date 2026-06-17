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


    rows = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return rows

