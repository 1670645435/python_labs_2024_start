import streamlit as st

# Create a title
st.title("Streamlit Test Wangziyi")

# Create a text input box
text_input = st.text_input("Enter some text:")

# Create a submit button
if st.button("Submit"):
    st.write("You've inputted:", text_input)