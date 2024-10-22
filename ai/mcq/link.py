import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to generate YouTube search URL based on the topic
def generate_youtube_search_url(topic):
    # Replace spaces in the topic with '+' for the URL format
    search_query = topic.replace(" ", "+")
    # YouTube search URL
    youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"
    return youtube_search_url

# Example usage in Streamlit
st.title("YouTube Study Links Generator")

# Get the topic from the user input
topic = st.text_input("Enter a topic to generate YouTube search link:", "webdevelopment")

if st.button("Generate YouTube Search Link"):
    # Generate the YouTube search URL based on the topic
    youtube_search_url = generate_youtube_search_url(topic)
    
    # Display the link
    st.write("Click the link below to search YouTube for your topic:")
    st.markdown(f"[Search YouTube for '{topic}']({youtube_search_url})", unsafe_allow_html=True)
