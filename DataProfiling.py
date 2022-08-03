import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

st.set_page_config(page_title = 'Data Profiler',layout='wide')

#sidebar
with st.sidebar:
    upload_file = st.file_uploader("upload .csv, .xlsx file not exceeding 10 mb")
    
if upload_file is not None:
    #time bing let load csv
    df = pd.read_csv(upload_file)
    
    #generate report
    with st.spinner("Generating Report"):
        pr = ProfileReport(df)
        
    st_profile_report(pr)