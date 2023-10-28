import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/16708c38-c755-4a1e-8c4b-ef3ec4910132/OOHmGfUtSR.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")
