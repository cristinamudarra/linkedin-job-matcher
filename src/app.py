import streamlit as st
from main import main_process

st.title("Discover your top 5 jobs available")

st.image("https://www.tmf-group.com/-/media/images/logos/case-study-logos/linkedin.png")
results = main_process()
st.write( results)



