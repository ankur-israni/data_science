import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

# Dataframe #1
df1 = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40],
})
st.write("Dataframe #1: ")
st.write(df1)

# Dataframe 2
data={
    "Name": ["John","Jane","Jake","Jill"],
    "Age":[28,24,36,42],
    "City":["New York","Los Angeles","Chicago","Houston"]
}
df2 = pd.DataFrame(data)
st.write("Dataframe #2: ")
st.write(df2)

# Save df2 to CSV
df2.to_csv("./resources/sample_data.csv")
st.write(df2)




# Create a line chart
# randn(20,3) = random numbers
# - 20 = number of rows
# - 3 = number of columns
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

# Create a textfield and echo whats typed in it.
txtName = st.text_input("Enter your name")
if txtName:
    st.write(f"Hello {txtName}")

# Slider
# Min value on slider = 0
# Max value on slider = 100
# Current value = 25
sliderAge = st.slider("Select your age: ",0,100,25)
st.write(f"Your age is {sliderAge}")


# Drop down list
options = ["Python","Java","C#"]
choice = st.selectbox("Choose your favourite language: ",options)
st.write(f"You selected {choice}")

# Upload file
uploaded_file = st.file_uploader("Choose a CSV file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)