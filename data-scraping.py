import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.common.by import By
import pandas as pd
import math 
# Ensure the proper version of ChromeDriver is installed
chromedriver_autoinstaller.install()

class LinkedInJobScraper:
    def __init__(self, job_title, location):
        self.job_title = job_title
        self.location = location
        self.List_Job_IDs = []
        self.driver = webdriver.Chrome()  # Change this to your preferred WebDriver
        self.user = 'cristinamudarrapradas@gmail.com'
        self.pwd = '532348290MaRiNaDoR!.'
        
    def log_in(self):
        # Open LinkedIn login page
        self.driver.get('https://www.linkedin.com/login')
        time.sleep(5)
        
        # Find the username and password fields by their IDs and input the credentials
        username_field = self.driver.find_element('id', 'username')
        password_field = self.driver.find_element('id', 'password')

        # Input your credentials
        username_field.send_keys(self.user)
        password_field.send_keys(self.pwd)

        # Submit the login form
        login_button = self.driver.find_element('xpath', '//button[@type="submit"]')
        login_button.click()

    def scroll_to_load_jobs(self, page_num=1, sleep_time=5):
        url = f'https://www.linkedin.com/jobs/search/?keywords={self.job_title}&location={self.location}&start={25 * (page_num - 1)}'
        self.driver.get(url)

        #self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        
        last_height = self.driver.execute_script('return document.body.scrollHeight')
        while True:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height
        time.sleep(sleep_time) 


    def find_job_id_aux(self, soup):
        Job_Ids_on_the_page = []
        job_postings = soup.find_all('li', {'class': 'jobs-search-results__list-item'})
        
        for job_posting in job_postings:
            Job_ID = job_posting.get('data-occludable-job-id')
            Job_Ids_on_the_page.append(Job_ID)
        
        return Job_Ids_on_the_page  
    
    
    
    def find_total_job_ids(self):
        print("Entered find_total_job_ids")
        # Parse the HTML content of the page using BeautifulSoup.
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # Get number of jobs found and number of pages:
        try:
            div_number_of_jobs = soup.find("div",{"class":"jobs-search-results-list__subtitle"})
            number_of_jobs = int(div_number_of_jobs.find('span').get_text().strip().split()[0])
        except:
            number_of_jobs = 0
            
        number_of_pages=math.ceil(number_of_jobs/25)
        print("number_of_jobs:", number_of_jobs)
        print("number_of_pages:", number_of_pages)
        

        
        # Get Job IDs that are on the first page:
        Jobs_on_1st_page = self.find_job_id_aux(soup=soup)
        print("Jobs on first page: ", Jobs_on_1st_page)
        self.List_Job_IDs.extend(Jobs_on_1st_page)
        
        # Iterate over the remaining pages:
        if number_of_pages > 1:
            
            for page_num in range(2,number_of_pages + 1):
                print(f"Scraping page: {page_num}",end="...")
                
                #url = f'https://www.linkedin.com/jobs/search/?keywords={self.job_title}&location={self.location}&start={25 * page_num}'
                #url = requests.utils.requote_uri(url)
                #self.driver.get(url)
                self.scroll_to_load_jobs(page_num=page_num)

                # Parse the HTML content of the page using BeautifulSoup.
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')

                # Get Job Ids present on the page.
                Jobs_on_this_page = self.find_job_id_aux(soup=soup)
                self.List_Job_IDs.extend(Jobs_on_this_page) 
        print("List_Job_IDs: ", self.List_Job_IDs)


    def scrape_job_details(self):
        def remove_tags(html):
            '''remove html tags from BeautifulSoup.text'''
        
            soup = BeautifulSoup(html, "html.parser")
        
            for data in soup(['style', 'script']):
                # Remove tags
                data.decompose()
        
            # return data by retrieving the tag content
            return ' '.join(soup.stripped_strings)
        job_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
        job={}
        list_jobs=[]

        for j in range(0, len(self.List_Job_IDs)):
            print(f"{j+1} ... read jobId:{self.List_Job_IDs[j]}")

            resp = requests.get(job_url.format(self.List_Job_IDs[j]))
            soup=BeautifulSoup(resp.text,'html.parser')
            #print(soup.prettify()) 

            job["Job_ID"] = self.List_Job_IDs[j] 
            
            try: 
                job["Job_txt"] = remove_tags(resp.content)
            except:
                job["Job_txt"] = None
            
            try:
                job["company"]=soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
            except:
                job["company"]=None

            try:
                job["job-title"]=soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
            except:
                job["job-title"]=None

            try:
                job["level"]=soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
            except:
                job["level"]=None

            try:
                job["location"]=soup.find("span",{"class":"topcard__flavor topcard__flavor--bullet"}).text.strip()
            except:
                job["location"]=None

            try:
                job["posted-time-ago"]=soup.find("span",{"class":"posted-time-ago__text topcard__flavor--metadata"}).text.strip()
            except:
                job["posted-time-ago"]=None

            try:
                nb_candidats = soup.find("span",{"class":"num-applicants__caption topcard__flavor--metadata topcard__flavor--bullet"}).text.strip()
                nb_candidats = int(nb_candidats.split()[0])
                job["nb_candidats"]= nb_candidats
            except:
                job["nb_candidats"]=None

            list_jobs.append(job)
            job={}

        # create a pandas Datadrame
        jobs_df = pd.DataFrame(list_jobs)

        return jobs_df

    def scrape_jobs(self):
        self.log_in()
        self.scroll_to_load_jobs()
        self.find_total_job_ids()
        job_df = self.scrape_job_details()
        self.driver.quit()  # Close the WebDriver
        return job_df