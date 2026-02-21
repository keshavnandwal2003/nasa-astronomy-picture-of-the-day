import streamlit as st
from get_data import get_data

data = get_data()
if data:
    st.title(data["title"])
    st.image(data["hdurl"])
    st.write(data["explanation"])
else:
    st.error("Failed to fetch data.")
