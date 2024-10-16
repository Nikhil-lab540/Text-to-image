import streamlit as st
import requests
import io
from PIL import Image

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

# Function to send the query to the Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
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
# Streamlit app layout

hide_streamlit_style()

st.title("Text to Image Generator")

# Input for text prompt
prompt = st.text_input("Enter a description to generate an image:", "")




# Submit button to generate the image
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            print(f"User input: {prompt}")
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

