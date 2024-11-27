import streamlit as st
from frontend.init_page import init_page

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    init_page()