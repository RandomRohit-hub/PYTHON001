import streamlit as st 
import pandas as pd
import numpy as np

## title of application
st.title("hello steamplit")    ##     cd streamlit  ---->  streamlit run app.py

## display a simple text
st.write('this is a simple text')

##create a simple data frame
df=pd.DataFrame({
    'first colum':[1,2,3,4],
    'second colum':[5,6,7,8,]
})

##display the data frame

st.write("here is the data frame")
st.write(df)

##craete a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)