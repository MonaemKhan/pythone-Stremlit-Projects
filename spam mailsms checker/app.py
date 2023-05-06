import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()  # lower case
    text = nltk.word_tokenize(text)  # tokenize
    y = []

    # Removing special characters
    for i in text:
        if i.isalnum():
            y.append(i)

    # remove special charecter and puntuation
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    # steming
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pk1','rb'))
model = pickle.load(open('model.pk1','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter The Message")

if st.button("Predict"):
    #1. preprocess
    transform_sms = transform_text(input_sms)
    #2. vectorize
    vector_input = tfidf.transform([transform_sms])
    #3. predict
    result = model.predict(vector_input)[0]
    #4. display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")