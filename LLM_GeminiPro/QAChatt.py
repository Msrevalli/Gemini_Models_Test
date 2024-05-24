# Import necessary libraries
from dotenv import load_dotenv  # To load environment variables from a .env file
import streamlit as st  # To create the web app
import os  # To interact with the operating system, especially for environment variables
import google.generativeai as genai  # To use Google's generative AI

# Load environment variables from a .env file
load_dotenv()

# Configure the generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the generative model and start a chat session
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Define a function to get a response from the Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Q&A Chat Application", page_icon="🔮")

# Initialize the chat history in session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input field for the user to enter their question
input = st.text_input("Input: ", key='input')

# Button for the user to submit their question
submit = st.button('Ask the question')

# If the submit button is clicked and there is input, get the response from the Gemini model
if submit and input:
    response = get_gemini_response(input)
    # Append the user's question to the chat history
    st.session_state['chat_history'].append(("You", input))
    
    # Display the response and append each chunk to the chat history
    st.subheader('Response:')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history
st.subheader('Chat History:')
for role, text in st.session_state['chat_history']:
    st.write(f'{role}: {text}')
