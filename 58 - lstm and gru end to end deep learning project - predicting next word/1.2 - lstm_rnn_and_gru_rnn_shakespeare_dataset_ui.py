import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the LSTM Model
model=load_model('./resources/dist/lstm_model.keras')

# Load the tokenizer
with open('./resources/dist/tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)

# Function to predict the next word
# - text: text entered by the user
# - token_list: numeric tokens for the input text
def predict_next_word(model, tokenizer, inputText, max_sequence_len):

    # Generate the numeric vector matrix for the given inputText
    numeric_vector_matrix_for_inputText = tokenizer.texts_to_sequences([inputText])[0]
    print(f"numeric_vector_matrix_for_inputText: {numeric_vector_matrix_for_inputText}")

    if len(numeric_vector_matrix_for_inputText) >= max_sequence_len:
        numeric_vector_matrix_for_inputText = numeric_vector_matrix_for_inputText[-(max_sequence_len-1):]  # Ensure the sequence length matches max_sequence_len-1
    
    # Pad the 'numeric_vector_matrix_for_inputText', so all inputText --to--> vector_matrix conversion is equal(i.e. 14 here) dimensions
    numeric_vector_matrix_for_inputText_padded = pad_sequences([numeric_vector_matrix_for_inputText], maxlen=max_sequence_len-1, padding='pre') 
    print('numeric_vector_matrix_for_inputText_padded',numeric_vector_matrix_for_inputText_padded)
    
    # Do prediction using the LSTM RNN model
    # - predicted_probabilites_for_each_word - Probabilities for all words in vocabulary to be the 'next' word
    predicted_probabilites_for_each_word = model.predict(numeric_vector_matrix_for_inputText_padded, verbose=0)
    print(f"predicted: {predicted_probabilites_for_each_word}") 

    # index_of_word_with_highest_probability - Find the index of the word with the highest probability - That is the next word according to our model
    index_of_word_with_highest_probability = np.argmax(predicted_probabilites_for_each_word, axis=1)
    print(f"index_of_word_with_highest_probability: {index_of_word_with_highest_probability}")

    # Find the word which has 'index_of_word_with_highest_probability'
    for word, index in tokenizer.word_index.items():
        if index == index_of_word_with_highest_probability:
            print('word = ',word)
            return word
    return None

# streamlit app
st.title("Next Word Prediction with LSTM / GRU")
input_text=st.text_input("Enter the sequence of Words","To be or not to")
if st.button("Predict Next Word"):
    max_sequence_len = model.input_shape[1] + 1  # Retrieve the max sequence length from the model input shape
    # print(f"model.input_shape[0]: {model.input_shape[0]}") # Output = 0
    # print(f"model.input_shape[1]: {model.input_shape[1]}") # Output = 13
    next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
    st.write(f'Next word: {next_word}')

