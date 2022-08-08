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




    
#for item in st.session_state.items():
#    item

#User authentication

names = ['OscarZeledon','DaniBlanco']
usernames = ['Oskir','Dblanco']
#passwords = ['Cestern22','12345']



#load hashed passwords
file_path = Path(__file__).parent / 'Hashed_pw.pkl'
with file_path.open('rb') as file:
    hashed_passwords = pickle.load(file)
   
#delete_all_cookies()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,'sales_dashboard', 'abcdef', cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login","sidebar")

#if authentication_status not in st.session_state:
#    authentication_status = st.session_state.authentication_status

if authentication_status == False:
    st.error('Username/Password is incorrect')
    
if authentication_status == None:
    st.error('Please enter your username and password')
    
if authentication_status == True:

    #sidebar

    
    with st.sidebar:
        upload_file = st.file_uploader("upload .xlsx file not exceeding 200 mb")
        authenticator.logout('Logout','sidebar')
        
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



        
        
