About:
    This is an opinion search engine on a database of Amazon Reviews.

Goal:
    Given a query containing one aspect and one opinion, we want to provide the most relevant reviews (semantically and contextually) from the database. 

Method:
    At least 2 methods will be used beyond a simple Boolean search (ie: N-gram based filtering, LDA, et cetera)

    Each method used can be assessed by its precision which is the percentage found by dividing the number of relevant postings by the total number of postings retrieved.

Implementation:
    
    Step 0: 
    Preprocessing

    Step 1:
    Create postings list by Doc ID

    Step 2:
    Get Boolean Search up and running

    Step 3:
    Find a way to search filter the reviews that mention the aspect in the orientation that is provided in the opinion.

Results: