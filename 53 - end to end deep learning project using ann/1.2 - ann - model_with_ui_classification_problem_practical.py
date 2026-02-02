'''
***Model and User Interface***
- This file combines the Model and the UI
- Model
    - Model built in file = '1.1 - ann - build_model_practical.ipynb' 
    - Model Algorithm used = ANN (Artificial Neural Network)
- UI
    - Framework = Streamlit
'''

import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Step 1 ) Load the trained models, encoders and scalars
# Load the ANN model
ann_model = tf.keras.models.load_model('./resources/pickle/1_ann_model.h5')

# Load the encoders and scalers
with open('./resources/pickle/1_label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('./resources/pickle/1_onehot_encoder_geography.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('./resources/pickle/1_standard_scaler_xtrain_xtest.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Step 2) Create the User Interface using Streamlit
st.title('Customer Churn Prediction')

# Step 2.1) Take User input
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0]) # onehot_encoder_geo.categories_[0] = ['France', 'Germany', 'Spain']
gender = st.selectbox('Gender', label_encoder_gender.classes_) # label_encoder_gender.classes_[1] = Male, label_encoder_gender.classes_[0] = Female
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])


# Step 3) - Create a DataFrame for the data entered 
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# Step 4 - Geography OneHotEncoding 
# Step 4.1) Encode Geography using OneHotEncoder
# Encoded Geography from [['France'], ['Germany'], ['Spain']] -----to----> [[1,0,0], [0,1,0], [0,0,1]] using OneHotEncoder
geo_encoded = onehot_encoder_geo.transform([[geography]]) 

# Step 4.2) Convert to Dataframe
# Output: geo_encoded_df = 
# Geography_France  Geography_Germany  Geography_Spain
#      1                 0                  0         
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))


# Step 4.3)  Combine one-hot encoded columns with input data
# Output: input_data =
#   CreditScore  Gender  Age  Tenure  Balance  NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  Geography_France  Geography_Germany  Geography_Spain
# 0          0.0       0   18       0      0.0              1          0               0              0.0               1.0                0.0              0.0
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)


# Step 5) Scale the input data
input_data_scaled = scaler.transform(input_data)
print(input_data_scaled)

# Step 6) Predict churn
prediction = ann_model.predict(input_data_scaled)
prediction_probability = prediction[0][0]
st.write(f'Churn Probability: {prediction_probability:.2f}')

if prediction_probability > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')
