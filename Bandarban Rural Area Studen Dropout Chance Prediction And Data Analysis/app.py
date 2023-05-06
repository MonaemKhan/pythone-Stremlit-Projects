import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")
import time

st.title('A Study of Predicting Student Dropout Using Machine Learning in Rural Areas of Bandarban Hill Tracts, Bangladesh')
cl = ['Class-1','Class-2','Class-3','Class-4','Class-5',
      'Class-6','Class-7','Class-8','Class-9','Class-10']
cl2 = ['Class-1','Class-2','Class-3','Class-4','Class-5',
      'Class-6','Class-7','Class-8','Class-9','Class-10','Class-11','Class-12']

clf = pickle.load(open('Model.pkl','rb'))

col1,col2 = st.columns(2)
with col1:
    stu_class = st.selectbox('Select Student Class',cl)
    fat_edu = st.selectbox("Select Father Education (Class)",cl2)
    mot_edu = st.selectbox('Select Mother Education (Class)',cl)
    edu_adut = st.text_input('No. of Educated Adult')
with col2:
    fat_income = st.text_input('Fother Income (Taka)')
    mot_income = st.text_input('Mother Income (Taka)')
    family_size = st.text_input('Total Family Member')
    neighbour = st.text_input('Total Surrounding Neighbour')

def CLass_level(CCl):
    count = 1
    for i in cl:
        if i == CCl:
            return count
        else:
            count = count+1
def CLass_level2(CCl):
    count = 1
    for i in cl2:
        if i == CCl:
            return count
        else:
            count = count+1

if st.button('Predict'):
    with st.spinner('Wait for it...'):
        time.sleep(5)
        s_class = CLass_level(stu_class)
        f_class = CLass_level2(fat_edu)
        m_class = CLass_level(mot_edu)

        stu_class = s_class
        fat_income = int(fat_income)
        fat_edu = f_class
        mot_income = int(mot_income)
        mot_edu = m_class
        family_size = int(family_size)
        edu_adut = int(edu_adut)
        neighbour = int(neighbour)

        data = [stu_class,fat_income,fat_edu,mot_income,mot_edu,
                family_size,edu_adut,neighbour]

        result = clf.predict([data])
        if result == 1:
            st.info('Child Will Go to School')
        else:
            st.info('Child Will Drop Out From School')

        result_prob = clf.predict_proba([data])
        col3, col4 = st.columns(2)
        with col3:
            st.success("Possibility of Going School : " + str(round(result_prob[0][1] * 100)) + '%')
        with col4:
            st.warning("Possibility of Drop Out From School : " + str(round(result_prob[0][0] * 100)) + '%')