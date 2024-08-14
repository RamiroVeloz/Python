import streamlit as st
from data_request import get_data

def data_sending (data : dict) -> dict [str,any]:
    
    characters : str = "characters"

    link : str = f"https://dragonball-api.com/api/{characters}/1"

    data : dict [str,any] = get_data(link)
    st.json(data)