import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from util import set_background

set_background('./bg/bg2.jpg')
st.title("พยากรณ์คะแนนจากชั่วโมงการเรียนของนักเรียน")
st.header("ตารางแสดงข้อมูลคะแนนการเรียนจากชั่วโมงการเรียน")

df=pd.read_csv('./data/score.csv')
st.write(df.head(10))

#st.line_chart(df)
#st.line_chart(df, x="interest_rate", y="unemployment_rate", color="stock_index_price")
st.header("Show Chart")
st.line_chart(
   df, x="Hours", y="Scores"  # Optional
)

x=df[['Hours']]
y=df['Scores']
pf=PolynomialFeatures(degree=3)
x_poly=pf.fit_transform(x)

x_train,x_test,y_train,y_test =train_test_split(x_poly,y, test_size=0.1,random_state=0)

modelRegress=LinearRegression()
modelRegress.fit(x_train,y_train)
x1=st.number_input("กรุณาป้อนข้อมูล ชั่วโมงการเรียน:")

if st.button("พยากรณ์ข้อมูล"):
    x_input=[[x1]]
    y_predict=modelRegress.predict(pf.fit_transform(x_input))
    st.write(y_predict)
    st.button("ไม่พยากรณ์ข้อมูล")
else:
    st.button("ไม่พยากรณ์ข้อมูล")

y_predict=modelRegress.predict(x_test)
df_predict_compare = pd.DataFrame({'y_test': y_test, 'y_predict': y_predict})

