import io

import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder

import streamlit as st

# interact with FastAPI endpoint
backend = "http://fastapi:8000/segmentation"


def process(image, server_url: str):

    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r


# construct UI layout
st.title("GPDB - General Purpose Dopamine Booster")

st.write(
    """Picture this. It is the year 2023, humanity has discovered a way to 
    automate 30% of the jobs. The influx of replaced workers floods the Internet.
    Companies learn to monetize based on the attention spam of these individuals.
    They are nothing more than information used to train a bigger system. 
    Money to be milked...
    Minds to be drained...
    Humanity is plugged already, call it "The Matrix" or "GPT". 
    There is no going back...
    """
)

st.write(
    """GPDB is a 10 year project. It is an attempt at understanding and exploiting human psycology.
    By focusing on research to replicate human behaviour, we hope to deepen our understanding of humanity. 
    By replacing labor, we hope to enhance labor. 
    You decrease the inputs while increasing outputs. 
    You let humans be humans. You let machines take over...
    And if we ever live in a world where humans are not needed...
    where machines are able to outlive us...
    why would it matter?
    Do you trust the stranger next to you to not consume you with their carnal desires?
    Maybe? You might have some false sense of security. 
    You might strongly believe in the system. 
    You have been conditioned in a world where action have consequences.
    Where the law is absolute and the constrains are real. 
    
    We are going to focus on systems that are absolute, vulnerable,
    exploitables, rich and profitables. 

    An ocean, where the treasure are vast, where potential is limitless. 
    Where actions are little but consequences big.

    Because persistency my friend, rocks, and consistency... always triumph.
    fortune favours the bold.


    Visit this URL at `:8000/docs` to understand what aspects of humanity are replaecable. """
)  # description and instructions

video_file = open('GPBD.mp4', 'rb') #enter the filename with filepath
video_bytes = video_file.read() #reading the file
st.video(video_bytes)

# Insert a chat message container.
with st.chat_message("user"):
    st.write("Hello 👋")
    st.write("I am Jose")
    #st.line_chart(np.random.randn(30, 3))

with st.chat_message("bot"):
    st.write("Hello 👋")
    st.write("I am the future")

# Display a chat input widget.
st.chat_input("Say something")

input_image = st.file_uploader("insert image")  # image upload widget

if st.button("Get segmentation map"):

    with st.spinner("Doing AI stuff ..."):
        col1, col2 = st.columns(2)

        if input_image:
            segments = process(input_image, backend)
            original_image = Image.open(input_image).convert("RGB")
            segmented_image = Image.open(io.BytesIO(segments.content)).convert("RGB")
            col1.header("Original")
            col1.image(original_image, use_column_width=True)
            col2.header("Segmented")
            col2.image(segmented_image, use_column_width=True)

        else:
            # handle case with no image
            st.write("Insert an image!")
