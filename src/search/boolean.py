#Boolean Search logic

def boolean_search_and(postings1, postings2):
    ### Conjunctive Boolean Search

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

def boolean_search_or(postings1, postings2):
    ### Disjunctive Boolean Search

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
    # Hard coded for OR AND OR. Time permitting, will generalize.

    [aspect, opinion] = query
    
    # Hard coded for 2 words per aspect. Time permitting, will generalize
    tokenized_aspect = aspect.lower().split()
    [aspect1, aspect2] = tokenized_aspect
    aspect1_list = postings.get(aspect1, [])
    aspect2_list = postings.get(aspect2, [])

    # Hard coded for 1 or 2 words per opinion. Time permitting, will generalize.
    tokenized_opinion = opinion.lower().split()
    if len(tokenized_opinion) == 2:
        [opinion1, opinion2] = tokenized_opinion
        opinion1_list = postings.get(opinion1, [])
        opinion2_list = postings.get(opinion2, [])
    else:
        opinion_list = postings.get(opinion, [])
    
    boolean_aspect = boolean_search_or(aspect1_list, aspect2_list)
    if len(tokenized_opinion) == 2:
        boolean_opinion = boolean_search_or(opinion1_list, opinion2_list)
    else:
        boolean_opinion = opinion_list

    boolean_search_result = boolean_search_and(boolean_aspect, boolean_opinion)

    return boolean_search_result


