import streamlit as st

st.set_page_config(page_title="Fake News Detection")

st.title("📰 Fake News Detection App")

news = st.text_area("Enter News Text")

if st.button("Predict"):
    if news.strip() == "":
        st.warning("Please enter some news text")
    else:
        st.success("App is Working Successfully!")