def build_stopwords_list():
    with open("stopwords.txt", "r", encoding="utf-8") as f:
        stopwords = {line.strip() for line in f if line.strip()}    
    return stopwords


    
