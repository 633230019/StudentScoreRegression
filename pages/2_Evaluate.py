import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

st.header("ตารางแสดงข้อมูลคะแนนการเรียนจากชั่วโมงการเรียน")
df=pd.read_csv("./data/score.csv")
st.write(df.head(10))

st.header("Show Chart")
st.line_chart(
   df, x="Hours", y="Scores"   # Optional
)

x=df[['Hours']]
y=df['Scores']
pf=PolynomialFeatures(degree=3)
x_poly=pf.fit_transform(x)

# Define a list of test sizes
test_sizes = [0.1, 0.2, 0.3, 0.4, 0.5]

# Example values for y_test and y_predict (replace with your actual values)
# Create an empty list to store the data for each test size
data_list = []

# Loop through test sizes and compute evaluation metrics
for test_size in test_sizes:
    x_train,x_test,y_train,y_test =train_test_split(x_poly,y, test_size=test_size, random_state=0)
    modelRegress=LinearRegression()
    modelRegress.fit(x_train,y_train)
    y_predict=modelRegress.predict(x_test)

    R2Score = r2_score(y_test, y_predict)
    MSE = mean_squared_error(y_test, y_predict)
    RMSE = np.sqrt(mean_squared_error(y_test,y_predict))
    split = str(int((1-test_size)*100))+"/"+str(int(test_size*100))
    
    # Create a dictionary with the values
    data = {'Data_split': split,'R2_Score': R2Score, 'MSE': MSE, 'RMSE': RMSE}
    
    # Append the data dictionary to the data_list
    data_list.append(data)

# Create a DataFrame from the list of data dictionaries
df_eval = pd.DataFrame(data_list)
st.header("ตารางเทียบผลการประเมินโมเดล")
st.write(df_eval)
split_ratios = df_eval['Data_split'].tolist()
rmse_values = df_eval['RMSE'].tolist()
mse_values = df_eval['MSE'].tolist()
r2_values = df_eval['R2_Score'].tolist()


x_train,x_test,y_train,y_test =train_test_split(x_poly,y, test_size=0.1,random_state=0)
modelRegress=LinearRegression()
modelRegress.fit(x_train,y_train)
y_predict=modelRegress.predict(x_test)
df_predict_compare = pd.DataFrame({'y_test': y_test, 'y_predict': y_predict})
st.header("ตารางเทียบผลการพยากรณ์คะแนนจากโมเดล 90/10")
st.write(df_predict_compare)