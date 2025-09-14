import pickle
import streamlit as st

model=pickle.load(open("loan.pkl","rb"))

def predictor():
    st.title("Loan Approval Prediction")

    no_of_dependents=st.number_input("NO.of dependents:")
    education=st.number_input("Enter 0:Graduate, 1:Not Graduate")
    self_employed=st.number_input("Enter Self employed:--0:No , 1:Yes")
    income_annum=st.number_input("Enter Annual Income:")
    loan_amount=st.number_input("Enter Loan Amo:")
    loan_term=st.number_input("Enter Loan term:")
    cibil_score=st.number_input("Enter Cibil Score:")
    residential_assets_value=st.number_input("Enter Residential Assests value:")
    commercial_assets_value=st.number_input("Enter Commercial Assests value:")
    luxury_assets_value=st.number_input("Enter Luxury Assests value:")
    bank_asset_value=st.number_input("Enter Bank Assests value:")


    pred=st.button("Submit")

    if pred:
        t=[no_of_dependents,education,self_employed,income_annum,loan_amount,loan_term,cibil_score,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value]
        op=model.predict([t])[0]
        if op==0:
            st.write("Approved")
        else:
            st.write("Rejected")

predictor()