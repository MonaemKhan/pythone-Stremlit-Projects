import numpy as np
import streamlit as st
import pickle
import sklearn

mod = pickle.load(open('Diabetes DT Bagging Model.pkl', 'rb'))

def process_data(Pregnancies,Glucose,BloodPressure,SkinThickness,
                 Insulin,BMI,DiabetesPedigreeFunction,Age):
    info = ''
    info = 'Pregnancies : ' + Pregnancies
    info = info + '\nGlucose : ' + Glucose
    info = info + '\nBloodPressure : ' + BloodPressure
    info = info + '\nSkinThickness : ' + SkinThickness
    info = info + '\nInsulin : ' + Insulin
    info = info + '\nBMI : ' + BMI
    info = info + '\nDiabetesPedigreeFunction : ' + DiabetesPedigreeFunction
    info = info + '\nAge : ' + Age
    info = info + '\n\nDecision : '

    Pregnancies = int(Pregnancies)
    Glucose = int(Glucose)
    BloodPressure = int(BloodPressure)
    SkinThickness = int(SkinThickness)
    Insulin = int(Insulin)
    BMI = float(BMI)
    DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
    Age = int(Age)

    N1 = 1
    if (Age <= 30 & Glucose <= 120):
        N1 = 0
    elif (Age > 30 & Age < 48 & Glucose <= 88):
        N1 = 0
    elif (Age >= 63 & Glucose <= 142):
        N1 = 0

    N2 = 1
    if (BMI <= 30):
        N2 = 0

    N3 = 1
    if (Age <= 27 & Pregnancies <= 6):
        N3 = 0
    elif (Age > 60 & Pregnancies > 7.5):
        N3 = 0

    N4 = 4
    if (Glucose <= 105 & BloodPressure <= 80):
        N4 = 0
    elif (Glucose <= 105 & BloodPressure > 83):
        N4 = 0

    N5 = 1
    if (SkinThickness <= 20):
        N5 = 0

    N6 = 1
    if (BMI < 30 & SkinThickness <= 20):
        N6 = 0
    elif (BMI > 33 & SkinThickness <= 20):
        N6 = 0

    N7 = 1
    if (Glucose <= 105 and BMI <= 30):
        N7 = 0
    elif (Glucose <= 105 and BMI >= 40):
        N7 = 0

    N9 = 1
    if (Insulin < 200):
        N9 = 0

    N10 = 1
    if (BloodPressure < 80):
        N10 = 0

    N11 = 1
    if (Pregnancies < 4 & Pregnancies != 0):
        N11 = 0

    N0 = BMI * SkinThickness
    N8 = Pregnancies / Age
    N13 = Glucose / DiabetesPedigreeFunction
    N12 = Age * DiabetesPedigreeFunction

    N15 = 1
    if (N0 < 1034):
        N15 = 0

    data = np.zeros(23)
    data[0] = Pregnancies
    data[1] = Glucose
    data[2] = BloodPressure
    data[3] = SkinThickness
    data[4] = Insulin
    data[5] = BMI
    data[6] = DiabetesPedigreeFunction
    data[7] = Age
    data[8] = N1
    data[9] = N2
    data[10] = N3
    data[11] = N4
    data[12] = N5
    data[13] = N6
    data[14] = N7
    data[15] = N9
    data[16] = N10
    data[17] = N11
    data[18] = N0
    data[19] = N8
    data[20] = N13
    data[21] = N12
    data[22] = N15

    result = mod.predict([data])
    proba = mod.predict_proba([data])

    if (result[0] == 1):
        st.error("You're At-Risk of Diabetes")
        st.warning("Chance of Diabetes : " + str(round(proba[0][1] * 100)) + "%")
        st.info("Chance of Not Diabetes : " + str(round(proba[0][0] * 100)) + "%")
        info = info+'\n'+"You're At-Risk of Diabetes"
        info = info + '\n'+"Chance of Diabetes : " + str(round(proba[0][1] * 100)) + "%"
        info = info + '\n'+"Chance of Not Diabetes : " + str(round(proba[0][0] * 100)) + "%"
        info = info + '\n\nSome Tips For You : '
        info = info + '\n' + '1.    Monitor blood sugar levels regularly'
        info = info + '\n' + '2.    Follow a healthy diet'
        info = info + '\n' + '3.    Engage in regular physical activity'
        info = info + '\n' + '4.    Take medication as prescribed'
        info = info + '\n' + '5.    Quit smoking'
        info = info + '\n' + '6.    Manage stress'
        info = info + '\n' + '7.    Get regular check - ups'
        flag = 1
    else:
        st.balloons()
        st.success("You're Safe Right Now")
        st.info("Chance of Not Diabetes : " + str(round(proba[0][0] * 100)) + "%")
        st.warning("Chance of Diabetes : " + str(round(proba[0][1] * 100)) + "%")
        info = info + '\n' + "You're Safe Right Now"
        info = info + '\n' + "Chance of Not Diabetes : " + str(round(proba[0][0] * 100)) + "%"
        info = info + '\n' + "Chance of Diabetes : " + str(round(proba[0][1] * 100)) + "%"
        info = info + '\n\nSome Tips For You : '
        info = info + '\n' + '1.    Monitor blood sugar levels regularly'
        info = info + '\n' + '2.    Follow a healthy diet'
        info = info + '\n' + '3.    Engage in regular physical activity'
        info = info + '\n' + '4.    Manage stress'
        info = info + '\n' + '5.    Get enough sleep'
        info = info + '\n' + '6.    Limit alcohol intake'
        info = info + '\n' + "7.    Don't smoke"
        flag = 0
    return flag,info