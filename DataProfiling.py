import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os
import datetime
from datetime import timedelta
import extra_streamlit_components as stx

st.set_page_config(page_title = 'Data Profiler',layout='wide')




    
import pickle
from pathlib import Path
import streamlit_authenticator as stauth



    #sidebar

st.write("## This Data Profiler tool has been developed by Oscar Zeledon")

with st.sidebar:
    upload_file = st.file_uploader("upload .csv or .xlsx files not exceeding 200 mb")
 #   authenticator.logout('Logout','sidebar')

    

if upload_file is not None:
    #time bing let load csv
    try:
        df = pd.read_excel(upload_file)
    except:
        df = df = pd.read_csv(upload_file)
    
    #generate report
    with st.spinner("Generating Report"):
        pr = ProfileReport(df)
        
    st_profile_report(pr)
    

        

#        try:
#            if authenticator.reset_password(username, 'Reset password', 'sidebar'):
#                st.success('Password modified successfully')
#        except Exception as e:
#            st.error(e)
        
#RESET PASSWORD WIDGET



        
        
