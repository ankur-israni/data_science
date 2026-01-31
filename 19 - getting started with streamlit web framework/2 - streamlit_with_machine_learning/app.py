import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier #Machine Learning Algorithm = Random Forest

@st.cache_data
def load_data():
    iris = load_iris()
    
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    print('df = ',df)
    print('iris.target = ',iris.target)
    print('iris.target_names = ',iris.target_names) # 1 Output Column / Target names with 3 possible outputs = setosa, versicolor, virginia

    df['species'] = iris.target  #A new column called 'species' is added (because of this statement), which represents the output_column/target
    return df,iris.target_names

# Load Iris data
# df = entire iris dataset
# target_name = 1 Output column with 3 possible outputs = setosa, versicolor, virginia
df,target_name = load_data()

model=RandomForestClassifier()

# Syntax: model.fit (x,y) where x = input_columns, y = output_columns
# input_columns = df.iloc[:,-1] = All columns except the last one - Expect the last one is signified as -1
# output_columns = df['species']
model.fit(df.iloc[:,:-1],df['species'])

st.sidebar.title("Input features")
sepal_length=st.sidebar.slider("Sepal Length",float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width=st.sidebar.slider("Sepal Width",float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petal_length=st.sidebar.slider("Petal Length",float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petal_width=st.sidebar.slider("Petal Width",float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))

input_data = [[sepal_length,sepal_width,petal_length,petal_width]]

# Prediction
prediction = model.predict(input_data)
predicted_species = target_name[prediction[0]]

st.write("Prediction")
st.write(f"The predicted speices is {predicted_species}")