import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity




def similarity(cv, df_jobs, top_offers=5):

    all_text = [cv] + list(df_jobs.Job_txt)
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_text)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    df_jobs["similarity"] = cosine_similarities
    df_jobs = df_jobs.sort_values(by='similarity', ascending=False)
    result = df_jobs[['company', 'job-title', 'level', 'location']].iloc[:top_offers]
    return result