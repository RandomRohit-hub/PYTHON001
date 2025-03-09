import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Streamlit Text Input")

# Create a text input field
name = st.text_input("Enter your name:")


# Display a personalized greeting if a name is entered
if name:
    st.write(f"Hello, {name}!")

# Display the input value
option =["pyhton","java","c++","javascript"]
choice=st.selectbox("choose your core language",option)

# Create a button to submit the form
age=st.slider("select ypur age",0,100,25)
st.write(f"your age is {age}")


data={
    "name":['john','jake','rex','jj'],
    'age':['22','22','17','12'],
    'city':['us','ncr','dd','uae']
}


df=pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)


uploaded=st.file_uploader('choose a csv file',type='csv')

if uploaded is not None:
    df=pd.read_csv(uploaded)
