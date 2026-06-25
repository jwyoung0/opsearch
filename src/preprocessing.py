from pathlib import Path
import nltk

def build_stopwords_list():
    project_root = Path(__file__).resolve().parent.parent       # For reliable paths
    stopwords_path = project_root / "stopwords.txt"
    
    with open(stopwords_path, "r", encoding="utf-8") as f:
        stopwords = {line.strip() for line in f if line.strip()}    
    
    return stopwords


    
