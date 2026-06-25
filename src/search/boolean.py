#Boolean Search logic

def boolean_search_and(postings, query, previous_result):
    ### Conjunctive Boolean Search

    [word1, word2] = query

    if previous_result == None:
        postings1 = postings.get(word1, [])
    else:
        postings1 = previous_result
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

def boolean_search_or(postings, query, previous_result):
    ### Disjunctive Boolean Search

    [word1, word2] = query

    if previous_result == None:
        postings1 = postings.get(word1, [])
    else:
        postings1 = previous_result
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
            result.append(postings1[index1])
            index1 += 1            
        else: 
            result.append(postings2[index2])
            index2 += 1      

    return result

def boolean_opsearch(postings, query):

    [aspect, opinion] = query
    tokenized_aspect = aspect.lower().split()
    tokenized_query = [tokenized_aspect, opinion]

    boolean_aspect = boolean_search_or(postings, tokenized_aspect, None)
  
    boolean_query_result = boolean_search_and(postings, tokenized_query, boolean_aspect)
   
    return boolean_query_result


