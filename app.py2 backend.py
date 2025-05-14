import streamlit as st
import requests

# Flask API endpoint
API_URL = "http://127.0.0.1:5000/predict"

st.title("Sentiment Analysis App")


# Text input
user_input = st.text_input("Enter a sentence to analyze its sentiment:")

if st.button("Predict"):
    if user_input:
        response = requests.post(API_URL, data={"text": user_input})
        if response.status_code == 200:
            result = response.json()
            sentiment = result["prediction"]
            confidence = result["confidence"]
            st.write(f"Predicted Sentiment: {sentiment}")
            st.write(f"Confidence Score: {confidence:.2f}")
        else:
            st.error("Error: Unable to get a response from the API.")
    else:
        st.warning("Please enter some text!")
