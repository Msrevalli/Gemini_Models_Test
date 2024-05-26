# MultiLanguage Invoice Extractor

This application allows users to upload an invoice image and get a detailed response about the invoice using Google's Generative AI model.

## Features
- Upload an image of an invoice (supported formats: jpg, jpeg, png).
- Enter a text prompt to get specific details about the invoice.
- Get a detailed response generated by the AI model based on the uploaded image and input prompt.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Msrevalli/Gemini_Models_Test.git
   
    cd Multilaguage_Invoice_Extractor_APP
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the project and add your Google API key:
    ```dotenv
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501`.

3. Upload an image of an invoice and enter your prompt.

4. Click the 'Tell me about the invoice' button to get a response.

## File Structure

- `app.py`: The main Streamlit application.
- `requirements.txt`: The list of dependencies required to run the application.
- `README.md`: This readme file providing information about the project.

## Dependencies

- `streamlit`: Web framework for creating interactive web applications.
- `python-dotenv`: To load environment variables from a `.env` file.
- `Pillow`: Python Imaging Library to open and manipulate image files.
- `google-generativeai`: Google's Generative AI library for generating responses based on input prompts.
