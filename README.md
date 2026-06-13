About:
    This is an opinion search engine on a database of Amazon Reviews.

Goal:
    Given a query containing one aspect and one opinion, we want to provide the most relevant reviews (semantically and contextually) from the database. We want to go beyond keyword retrieval (semantic only) and get to opinion (contextual) retrieval.

Method:
    At least 2 methods will be used beyond a simple Boolean search (ie: N-gram based filtering, LDA, et cetera)

    Each method used can be assessed by its precision which is the percentage found by dividing the number of relevant postings by the total number of postings retrieved.

Implementation:
    
    Step 0: 
    Preprocessing
    - Filtering
        - Those appearing less than 5 times
        - Stops words from https://gist.github.com/sebleier/554280
    - Lemmatization/stemming
    - Smiley faces, (emojis?), and their variations using regular expressions, et cetera

    Step 1:
    Create postings list by Doc ID

    Step 2:
    Get Boolean Search up and running

    Step 3:
    Find a way to search filter the reviews that mention the aspect in the orientation that is provided in the opinion.

Results:

6.12.26
    I downloaded DBeaver in order to create a database connection and create a database with the SQL dump. I created a database in MySQL CLI, then I connected it to DBeaver.