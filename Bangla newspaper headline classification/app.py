import streamlit as st
import preprocessing_model as pm
st.header('"বাংলা সংবাদপত্রের খবর শ্রেনীকরণ"')
file = st.text_area("সংবাদটি লিখুন ( অবশ্যই বাংলা সংবাদ)")

if st.button('যাচাই করুন'):
	st.header('এই সংবাদটি "'+pm.process(file)+'" শ্রেনীতে পড়েছে')


