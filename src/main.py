from components.datascraping import LinkedInJobScraper
from components.readcv import get_pdf
from components.similarity import similarity
from components.data_preprocessing import keep_letters, delete_beginning_end
import pandas as pd


def main_process(cv):
    # job_offers = scrape_linkedin(job_title="Data scientist", location="New York")
    job_offers = pd.read_pickle("data/scraped_data/df_data_science.pkl")
    job_offers = job_offers.drop_duplicates()
    job_offers["Job_txt"] = job_offers.Job_txt.apply(delete_beginning_end)
    job_offers["Job_txt"] = job_offers.Job_txt.apply(keep_letters)

    # user_cv_path = "data/CV Cristina Mudarra.pdf"
    cv = get_pdf(cv)
    cv = cv.replace("\n", " ")
    cv = keep_letters(cv)

    top_similar_jobs = similarity(cv, job_offers, 5)

    return top_similar_jobs

