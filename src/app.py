import streamlit as st
from main import main_process

st.title("Discover your top 5 jobs on")

st.image("https://www.tmf-group.com/-/media/images/logos/case-study-logos/linkedin.png", width=300)
# results = main_process()
# st.write(results)


def main():
    st.write(
        "Welcome to the LinkedIn Job Matcher tool. This platform assists you in discovering relevant job opportunities based on your professional profile. We conduct web scraping of job listings on LinkedIn, utilizing the gathered information to provide tailored recommendations."
    )
    st.write("**How it works:**")
    st.write(
        "**1. Job Listings Search:** We scrape job postings on LinkedIn for a specific role and location."
    )
    st.write(
        "**2. Upload Your Resume:** Enter your curriculum vitae to receive personalized recommendations."
    )
    st.write(
        "**3. Customized Results:** We analyze job details, compare the skills and requirements with your CV, and present the 5 most similar job postings, offering opportunities aligned with your expertise."
    )
    uploaded_file = st.file_uploader(
        "Insert your Resume in pdf format.", type="pdf"
    )

    jobs = ['Data scientist', 'Data analyst', 'Data engineer', 'Machine learning engineer', 'Business analyst']
    locations = ["New York","London", "Dublin", "Edinburgh", "California",  "Chicago", "Sidney"]

    option_job = st.selectbox('Select a job:', jobs)
    option_city = st.selectbox('Select a city:', locations)
    
    if uploaded_file is not None and option_job is not None and option_city is not None:
        st.write("Top 5 jobs aligned with your CV:")
        results = main_process(uploaded_file, option_job, option_city)
        blankIndex=[''] * len(results)
        results.index=blankIndex
        st.table(results)


if __name__ == "__main__":
    main()
