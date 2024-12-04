import joblib
import pandas as pd
import numpy as np
import streamlit as st

Model = joblib.load(r"E:\FCI\4th year\1\Machine Learning\Machine Learning\Machine Projects\SVM model with employee data set\SVM model.pkl")
Inputs = joblib.load(r"E:\FCI\4th year\1\Machine Learning\Machine Learning\Machine Projects\SVM model with employee data set\Inputs.pkl")

def prediction(Education,JoiningYear,City,PaymentTier,Age,Gender,EverBenched,ExperienceInCurrentDomain):
    df = pd.DataFrame(columns=Inputs)
    df.at[0,"Education"] = Education
    df.at[0,"JoiningYear"] = JoiningYear
    df.at[0,"City"] = City
    df.at[0,"PaymentTier"] = PaymentTier
    df.at[0,"Age"] = Age
    df.at[0,"Gender"] = Gender
    df.at[0,"EverBenched"] = EverBenched
    df.at[0,"ExperienceInCurrentDomain"] = ExperienceInCurrentDomain
    result = Model.predict(df)[0]
    return result

def Main():
    st.title("Leave or Not Leave My Lovely Company Prediction")
    Education = st.selectbox("Education",['Bachelors', 'Masters' , 'PHD'])
    JoiningYear = st.slider("JoiningYear",min_value=2012.0 , max_value=2018.0 , step=1.0,value = 2012.0)
    City = st.selectbox("City",[ 'Bangalore',  'Pune',  'New Delhi'])
    PaymentTier = st.selectbox("PaymentTier",[ '1',  '2',  '3'])
    Age = st.slider("Age",min_value=20.0 , max_value=60.0 , step=1.0,value = 20.0)
    Gender = st.selectbox("Gender",['Male', 'Female'])
    EverBenched = st.selectbox("EverBenched",['Yes','No'])
    ExperienceInCurrentDomain = st.slider("ExperienceInCurrentDomain",min_value=0.0 , max_value=7.0 , step=1.0,value = 0.0)
    
    
    if st.button("Predict"):
        result = prediction(Education,JoiningYear ,City,PaymentTier,Age,Gender,EverBenched,ExperienceInCurrentDomain)
        list_result = ["Not Leave" , "Leave"]
        st.text(f"Your Employee Will {list_result[result]}")
Main()