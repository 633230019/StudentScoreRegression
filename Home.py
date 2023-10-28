import json
import time
import requests
from util import set_background
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

st.set_page_config(
    page_title="Datascience Project",
    page_icon= ":bar_chart:",
)
set_background('./bg/bg5.png')
st.sidebar.success("เลือกรายการด้านบน.")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.header("💯พยากรณ์คะแนนการเรียนจากเทคนิค Linear Regression!💯")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_book = "https://lottie.host/16708c38-c755-4a1e-8c4b-ef3ec4910132/OOHmGfUtSR.json"
lottie_book = load_lottieurl(lottie_url_book)
st_lottie(lottie_book, key="book")

st.header("📝📝📝")
st.header("โดย นายสิทธิพงษ์ แจ้งไพร")
st.header("รหัสนักศึกษา 633230019 หมู่เรียน 24.2")
st.header("สาขาเทคโนโลยีสารสนเทศ")
st.header("คณะวิทยาศาสตร์และเทคโนโลยี")
st.header("มหาวิทยาลัยราชภัฏนครปฐม")
st.balloons()