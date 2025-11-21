from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st,pandas as pd
def sa(text):
    analyzer=SentimentIntensityAnalyzer()
    if text and text.strip(): 
        score=analyzer.polarity_scores(text)
        return score
    else:
        return 'Please enter some text'



st.set_page_config(layout='wide')

if 'logged_in' not in st.session_state:
    st.session_state.logged_in=False

def login_page():
    with st.form('Login'):
        username=st.text_input('Please enter your username',key='username1')
        password=st.text_input('Password',type='password',key='password1')
        submit=st.form_submit_button('Submit')
        if submit:
            if username=='admin' and password=='password':
                st.session_state.logged_in=True
            else:
                st.error('Invalid Credentials')

def welcome():
    st.title('Simple Sentiment Analyser')
    text=st.text_area('Please enter some text')
    if st.button('Submit',key='welcome1'):
        st.dataframe(sa(text))

if st.session_state.logged_in:
    welcome()
else:
    login_page()