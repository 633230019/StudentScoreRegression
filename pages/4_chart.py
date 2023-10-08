import streamlit as st
import pandas as pd

st.header("Show Data Index Price")
df=pd.read_csv("./data/score.csv")
st.write(df.head(10))

st.header("Show Chart")
st.line_chart(
   df, x="Hours", y="Scores", color=["#FF0000", "#0000FF"]  # Optional
)

