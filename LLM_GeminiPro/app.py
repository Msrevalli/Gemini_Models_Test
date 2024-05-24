# Import necessary libraries
from dotenv import load_dotenv  # To load environment variables from a .env file
import streamlit as st  # To create the web app
import os  # To interact with the operating system, especially for environment variables
import google.generativeai as genai  # To use Google's generative AI

# Load environment variables from a .env file
load_dotenv()

# Configure the generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Define a function to get a response from the Gemini model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app header
st.header('Gemini LLM Application')

# Input field for the user to enter their question
input = st.text_input("Input: ", key='input')

# Button for the user to submit their question
submit = st.button('Ask the question')

# If the submit button is clicked, get the response from the Gemini model and display it
if submit:
    response = get_gemini_response(input)
    st.write(response)
