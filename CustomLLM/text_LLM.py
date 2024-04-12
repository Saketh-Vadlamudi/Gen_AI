

import streamlit as st
import os
import google.generativeai as genai

#get api keys from gemini ai
genai.configure(api_key='')

model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response1 = model.generate_content(question)
    return response1.text
st.set_page_config(page_title = 'Project')
st.header('Gemini LLM Application')
input = st.text_input('Input: ',key = 'input')
submit = st.button('Ask me')
if submit:
    response=get_gemini_response(input)
    st.subheader('The response is')
    st.write(response)


