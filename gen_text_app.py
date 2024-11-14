import streamlit as st 

import pathlib
import textwrap
import os

from IPython.display import display
from IPython.display import Markdown

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key=API_KEY)

def text_generation(input):
        
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(input)

    var = to_markdown(response.text)
    # print(var)

    # print(response.text)
    result = response.text
    return result



def footer():

    st.markdown("---")
    st.markdown("### About")
    st.markdown("This is a question answering app you can ask anything...")
    st.markdown("Developed by Atul Purohit")


