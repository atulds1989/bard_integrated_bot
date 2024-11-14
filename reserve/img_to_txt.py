import pathlib
import textwrap
import os
import PIL.Image
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

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)




img = PIL.Image.open(r'C:\Users\hp\OneDrive\Pictures\Screenshots\asura.jpg')
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
print(img)

# to_markdown(response.text)
print(response.text)