import re
import pandas as pd
from nltk.corpus import stopwords



def delete_beginning_end(text):
    match = re.search(r'Report this job (.+)', text)
    temp_text = match.group(1).strip()

    cleaned_text = re.sub(r'Show more Show less.*', '',temp_text)
    cleaned_text = cleaned_text.strip()
        
    return cleaned_text

def keep_letters(text):
    pattern = re.compile(r"[^a-z\s]", re.I)
    return re.sub(pattern, ' ', text)




