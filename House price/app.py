import streamlit as st
import json
import pickle
import numpy as np
import sklearn

st.title("House Price Prediction")

total_sqft = st.text_input("Enter Requried Sqft",placeholder="1000",max_chars=5)

bhk = st.radio(
    'Total Bedroom',
    (1,2,3,4,5,6),horizontal=True)

bath = st.radio(
    'Total Bathroom',
    (1,2,3),horizontal=True)

data_columns = json.load(open('columns.json','r'))['data_columns']

location = st.selectbox('Location',data_columns[3:])

model = pickle.load(open('bangalore_home_price_model.pickle','rb'))


if st.button("Predict Price"):
    if total_sqft == "":
        total_sqft = "1000"
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = float(total_sqft)
    x[1] = int(bath)
    x[2] = int(bhk)
    if loc_index >= 0:
        x[loc_index] = 1

    estimated_price = round(model.predict([x])[0],2)
    msg = "Estimated price of flat is: "+str(estimated_price)
    st.subheader(msg)