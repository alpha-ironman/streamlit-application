import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("Welcome to your simple Streamlit application!")

# User input
name = st.text_input("Enter your name:")

# Button action
if st.button("Submit"):
    st.success(f"Hello, {name} 👋")

# Slider example
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")
