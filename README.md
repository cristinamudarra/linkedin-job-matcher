# LinkedIn Job Matcher

# Overview
The LinkedIn Job Matcher is at a Minimum Viable Product (MVP) stage. It is designed to streamline the job search process for users by providing personalized job recommendations based on their uploaded CV. The project's uniqueness lies in its ability to read various CV formats, breaking away from the constraints of a common and structured template. The system focuses on data-related roles, including data scientist, data analyst, data engineer, machine learning engineer, and business analyst, within specific locations such as London, New York, Dublin, Edinburgh, Chicago, California, and Sydney.

The project workflow involves several key stages:

# Features
##  1. Web Scraping for Job Data:

  - The system performs web scraping of LinkedIn job postings every 24 hours.
  - Collected information includes job description, job title, company, number of applicants, posting date, and location.
    
##  2. NLP Text Processing:

  - Job descriptions are processed using advanced Natural Language Processing (NLP) techniques.
  - Text cleaning, TF-IDF embeddings, and stemming are applied to enhance the accuracy of job matching.

##  3. User Input and CV Attachment:

  - Users can choose a specific job title and location.
  - They have to attach their CV in PDF format.
    
##  4. PDF Text Extraction:

- The system processes the attached PDF CV, converting it into readable text for analysis.
  
##  5. Job Scoring and Recommendations:

  - A scoring system evaluates the user's background against existing job opportunities.
  - The user receives personalized recommendations, consisting of the top 5 jobs that align with their skills and preferences.

# Usage
Clone the repository:

##  1. Clone the repository:
    git clone https://github.com/cristinamudarra/linkedin-job-matcher.git
##  2. Install dependencies:
    pip install -r requirements.txt
##  3. Run the application:
    python app.py

# Requirements
  - Python 3.7 or later
  - Dependencies listed in requirements.txt

# Contributing
Feel free to contribute by opening issues or submitting pull requests. 



