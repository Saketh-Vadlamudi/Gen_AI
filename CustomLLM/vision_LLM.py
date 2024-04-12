import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

##get api keys from gemini ai
genai.configure(api_key='')

model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image):
    if input!='':
        response1= model.generate_content([input,image])
    else:
        response1 = model.generate_content(image)
    return response1.text
st.set_page_config(page_title = 'Project')
st.header('Gemini LLM Application')
input = st.text_input('Input: ',key = 'input')

uploaded_file = st.file_uploader('Choose an image:',type=['jpg','png','jpeg'])
image=''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='Uplaod Image,',use_column_width=True)
submit = st.button('Give details')
if submit:
    response = get_gemini_response(input,image)
    st.subheader('The data is')
    st.write(response)
