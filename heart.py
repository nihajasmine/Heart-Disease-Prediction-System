import pickle
import streamlit as st

model=pickle.load(open("heart.pkl","rb"))

def predictor():
    st.title("Heart Prediction")

    Age=st.number_input("1.Enter age--------")
    Sex=st.number_input("2.Enter sex ---------Female=0, Male=1")
    Chest_Pain_Type=st.number_input("3.Chest pain Type ---- Asymptomatic=0, Atypical angina=1, Non-anginal pain=2, Typical angina=3")
    Rest_BP=st.number_input("4.Enter Resting BP------")
    Cholestrol=st.number_input("5.Enter cholestoral------")
    FBS=st.number_input("6.Enter fasting blood sugar----- lessthan 120=1, greaterthan 120=0")
    RestECG=st.number_input("7.Enter rest ECG---- Left ventricular hypertrophy=0,  Normal=1,  ST-T wave abnormality=2")
    MaxHR=st.number_input("8.Enter max heart rate-------")
    EIA=st.number_input("9.Enter exercise induced angina------ yes=1 and no=0")
    oldpeak=st.number_input("10.Enter oldpeak-----")
    Slope=st.number_input("11.Enter slope--------- downsloping=0, flat=1, upsloping=2")
    Vessels_color=st.number_input("12.Enter vessels colored by flourocopy--- 0 or 1 or 2 or 3 or 4")
    Thalassemia=st.number_input("13.Enter Thalassemia-------- Fixed defect=0, Normal=1, Reversable Defect=2")

    pred=st.button("Submit")

    if pred:
        op=model.predict([[Age,Sex,Chest_Pain_Type,Rest_BP,Cholestrol,FBS,RestECG,MaxHR,EIA,oldpeak,Slope,Vessels_color,Thalassemia]])[0]
        if op==0:
            st.write("NO HEART DISEASE")
        else:
            st.write("HEART DISEASE")

predictor()