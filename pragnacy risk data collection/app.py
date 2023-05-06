import streamlit as st
import pandas as pd

def convert_to_metre(height):
    try:
        height = height.split('.')
        feet_to_metre = (int) (height[0])*0.3048
        inchie_to_metre = (int) (height[1])*0.0254
        return feet_to_metre+inchie_to_metre
    except:
        feet_to_metre = (int)(height[0]) * 0.3048
        return feet_to_metre

st.title("Pragnancy Risk Data Collection")
col1,col2,col3 = st.columns(3)
with col1:
    age = st.text_input("Age:")
    para = st.text_input("Para")
    gravida = st.text_input("Gravida")
    delivary = st.selectbox('Delivary type',['No_delivary','Normal','C-section'])
    height = st.text_input('Height')
with col2:
    bloodgroop = st.selectbox("is blood group Negative",['No','Yes'])
    up_presure = st.text_input("Systolic Blood Pressure")
    dn_preseue = st.text_input("Diastolic Blood Pressue")
    weight = st.text_input('Weight')
    edema = st.selectbox("Edema",['Normal','Modarate','High'])
with col3:
    anemia = st.selectbox("Anemia",['Normal','Low','Very-Low'])
    jondis = st.selectbox("Jaundice",['No','Yes'])
    diabaties = st.selectbox('Diabetes',['No','Yes'])
    risk = st.selectbox('Risk',['No','Yes'])
    if st.button('Calculate BMI'):
        bmi = round((float(weight) / convert_to_metre(height) ** 2), 2)
        if bmi <= 18.5:
            st.text("BMI: " + str(bmi) + " underweight.")
        elif 18.5 < bmi <= 24.9:
            st.text("BMI: " + str(bmi) + " normal.")
        elif 25 < bmi <= 29.29:
            st.text("BMI: " + str(bmi) + " overweight.")
        else:
            st.text("BMI: " + str(bmi) + " obese.")


if st.button("Add Information"):
    data = {
        'Age': [int(age)],
        'Height': [round(float(convert_to_metre(height)),3)],
        'Weight': [round((float(weight)),2)],
        'BMI': [round((float(weight) / convert_to_metre(height) ** 2), 2)],
        'Blood Group ( is Negative?)': [bloodgroop],
        'Delivery Type': [delivary],
        'Systolic Blood Pressure': [int(up_presure)],
        'Diastolic Blood Pressure': [int(dn_preseue)],
        'Edema': [edema],
        'Anemia': [anemia],
        'Jaundice': [jondis],
        'Diabetes': [diabaties],
        'Risk': [risk],
        'Para':[int(para)],
        'Gravida':[int(gravida)]
    }
    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.text('View of Data')
    st.table(data)
    try:
        df = pd.read_csv('Pregnancy Risk.csv')
        df2 = pd.DataFrame(data)
        df3 = pd.concat([df, df2], axis=0, join='inner')
        df3.to_csv('Pregnancy Risk.csv')
        st.subheader("Store Successfull")
        st.table(df3.tail(3))
    except:
        st.subheader('Problem')