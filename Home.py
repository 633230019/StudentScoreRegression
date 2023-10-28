import json
import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

st.set_page_config(
    page_title="Datascience Project",
    page_icon= ":bar_chart:",
)
st.sidebar.success("เลือกรายการด้านบน.")

st.title("💯พยากรณ์คะแนนการเรียนจากเทคนิค Linear Regression!💯")
st.write("")
st.header("📝 โดย นายสิทธิพงษ์ แจ้งไพร")
st.header("รหัสนักศึกษา 633230019 หมู่เรียน 24.2")
st.header("สาขาเทคโนโลยีสารสนเทศ")
st.header("คณะวิทยาศาสตร์และเทคโนโลยี")
st.header("มหาวิทยาลัยราชภัฏนครปฐม")
st.balloons()