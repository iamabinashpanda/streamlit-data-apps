import streamlit as st

st.title("Demo Project 1")
st.markdown("---")

tab1,tab2 = st.tabs(["Tab 1", "Tab 2"])

if st.button("Submit"):
    st.balloons()