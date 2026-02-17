# Step 1: Import Libraries and Load the Model
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load the pre-trained model with ReLU activation
model = load_model('./resources/dist/2_simple_rnn_model.h5')

# Step 2: Helper Functions
# Function to decode reviews
# e.g. Input = encoded_review = [1, 14, 22, 16, 43]
# Output = "? this film was great"
'''
 - i - 3 → adjusts for IMDB’s index offset
 - reverse_word_index → maps number → word
 - '?' → used if word not found

 This function is not used in the example.
'''
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

'''
e.g. Input = text = "This movie was great"
e.g. Output = [[1, 14, 22, 16, 43, 0, 0, 0, ..., 0]] (padded and encoded review)
'''
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review


# Streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')

# User input
user_input = st.text_area('Movie Review')

if st.button('Classify'):

    preprocessed_input=preprocess_text(user_input)

    ## Make prediction
    prediction=model.predict(preprocessed_input)
    sentiment='Positive' if prediction[0][0] > 0.5 else 'Negative'

    # Display the result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please enter a movie review.')

