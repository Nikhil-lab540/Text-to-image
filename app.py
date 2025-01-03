import streamlit as st
import requests
import io
from PIL import Image
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/XLabs-AI/flux-RealismLora"
headers = {"Authorization": "Bearer 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"}

# Function to send the query to the Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.text)  # Log the response content for debugging
    return response.content



def hide_streamlit_style():
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

hide_streamlit_style()
# Streamlit app layout
st.title("Text to Image Generator")

# Input for text prompt
prompt = st.text_input("Enter a description to generate an image:", "")

# Submit button to generate the image
if st.button("Generate Image"):
    if prompt:
        # Log user input (works locally but not visible on cloud deployment)
        logger.info(f"User input: {prompt}")

        with st.spinner("Generating image..."):
            try:
                # Call the API and get the image
                image_bytes = query({"inputs": prompt})

                # Load and display the image using PIL
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption=f"Generated Image for: {prompt}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before generating an image.")
