import streamlit as st

st.title("Demo Project 1")
st.markdown("---")

tab1,tab2 = st.tabs(["Tab 1", "Tab 2"])

tab1.write('Hello World')

st.header('st.button')

if st.button("Click me"):
    st.write('Click me')
else:
    st.write('Hello World')