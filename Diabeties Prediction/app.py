import warnings
warnings.filterwarnings("ignore")
from process_model import process_data
import streamlit as st
import time
from PIL import Image

st.set_page_config(
    page_title="Diabetes Prediction",
    layout="wide"
)

flag = -1
st.title("Diabetes Prediction")
col1, col2 = st.columns(2)

info = 'No Info Right Now.\nEnter Your Info 1st'

with st.form("my_form"):
    with col1:
        Pregnancies = st.text_input('Number Of times pregnant(0 - 17)')
        Glucose = st.text_input('Oral Glucose Tolerance Test (2 hour)(44 - 199)')
        BloodPressure = st.text_input('Diastolic Blood Pressure (mm Hg)(24 - 122)')
        SkinThickness = st.text_input('Triceps Skin Fold Thickness (mm)(7 - 99)')
    with col2:
        Insulin = st.text_input('2-Hour Serum Insulin (micro U/ml(0 - 846)')
        BMI = st.text_input('Body Mass Index (BMI)(18.2 - 67.1)')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function(0.078 - 2.42)')
        Age = st.text_input('Age in Years(21 - 81)')

    col3, col4,col5 = st.columns(3)
    with col3:
        submitted = st.form_submit_button(label="Submit")
        if submitted:
            with st.spinner('Wait for the result'):
                time.sleep(5)
                flag,info = process_data(Pregnancies, Glucose, BloodPressure, SkinThickness,
                                Insulin, BMI, DiabetesPedigreeFunction, Age)
    with col5:
        if flag == 1:
            st.header('Suggestion')
            st.write('1.    Monitor blood sugar levels regularly')
            st.write('2.    Follow a healthy diet')
            st.write('3.    Engage in regular physical activity')
            st.write('4.    Take medication as prescribed')
            st.write('5.    Quit smoking')
            st.write('6.    Manage stress')
            st.write('7.    Get regular check - ups')
        elif flag ==0:
            st.header('Suggestion')
            st.write('1.    Maintain a healthy weight')
            st.write('2.    Follow a healthy diet')
            st.write('3.    Engage in regular physical activity')
            st.write('4.    Manage stress')
            st.write('5.    Get enough sleep')
            st.write('6.    Limit alcohol intake')
            st.write("7.    Don't smoke")

st.download_button(
    label="Download Information",
    data=info,
    file_name='info.txt',
    mime='text/plain',
)

if st.button('Show Diet Chat'):
    col3, col4, col5 = st.columns(3)
    with col4:
        image = Image.open('diabetes.png')
        st.image(image)