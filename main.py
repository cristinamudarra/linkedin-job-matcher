from src.datascraping import LinkedInJobScraper
from src.readcv import get_pdf
from src.similarity import similarity
from src.data_preprocessing import keep_letters, delete_beginning_end
import pandas as pd

def main():
    
    #job_offers = scrape_linkedin(job_title="Data scientist", location="New York")
    job_offers = pd.read_pickle('data/scraped_data/df_data_science.pkl')
    job_offers = job_offers.drop_duplicates()
    job_offers['Job_txt'] = job_offers.Job_txt.apply(delete_beginning_end)
    job_offers['Job_txt'] = job_offers.Job_txt.apply(keep_letters)
    

    user_cv_path = "data\CV Cristina Mudarra.pdf"
    cv = get_pdf(user_cv_path)
    cv = cv.replace("\n", " ")
    cv = keep_letters(cv)

    top_5_similar_jobs = similarity(cv, job_offers, 5)
    
    print(top_5_similar_jobs)


if __name__ == "__main__":
    main()
