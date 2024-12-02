import google.generativeai as genai
import streamlit as st

google_api_key="AIzaSyBfd9L7ISpM03ysx7rtCmI2B5coguKmUNQ"
genai.configure(api_key=google_api_key)

model=genai.GenerativeModel('gemini-pro')

def gemini_response(question):
    response=model.generate_content(question)
    return response

st.set_page_config(page_title="Demo")
st.header("Model Dummy")
input=st.text_input("inp:",key='input')
submit=st.button("Go")

if submit:
    response=model.generate_content(input)
    st.subheader('Response')
    st.write(response)
   
