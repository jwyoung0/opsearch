from write import print_reviews_by_id

def boolean_search(postings, query):
    ### Conjunctive Boolean Search

    [word1, word2] = query

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