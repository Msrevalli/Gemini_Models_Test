# Import necessary libraries
from dotenv import load_dotenv  # To load environment variables from a .env file
import streamlit as st  # To create the web app
import os  # To interact with the operating system, especially for environment variables
import google.generativeai as genai  # To use Google's generative AI
from PIL import Image  # To work with images

# Load environment variables from a .env file
load_dotenv()

# Configure the generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro-vision')

# Define a function to get a response from the Gemini model
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Gemini Image Application", page_icon="🔮")

# Streamlit app header
st.header('Gemini LLM Application')

# Input field for the user to enter their question
input = st.text_input("Input: ", key='input')

# File uploader for the user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key='image')
image = ''

# If an image is uploaded, display it
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Button for the user to submit their question
submit = st.button('Tell me about the image')

# If the submit button is clicked, get the response from the Gemini model and display it
if submit:
    response = get_gemini_response(input, image)
    st.subheader('Response:')
    st.write(response)
