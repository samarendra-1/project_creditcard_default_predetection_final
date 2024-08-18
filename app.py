import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))



# Streamlit app
st.title("Credit Card Default Prediction")
feature_names = [
    "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE",
    "PAY_SEPT", "PAY_AUG", "PAY_JUL", "PAY_JUN", "PAY_MAY", "PAY_APR",
    "BILL_AMT_SEPT", "BILL_AMT_AUG", "BILL_AMT_JUL", "BILL_AMT_JUN", "BILL_AMT_MAY", "BILL_AMT_APR",
    "PAY_AMT_SEPT", "PAY_AMT_AUG", "PAY_AMT_JUL", "PAY_AMT_JUN", "PAY_AMT_MAY", "PAY_AMT_APR"
]

# Create a form to input values
with st.form("Credit_Card_Form"):
    limit_bal = st.number_input("LIMIT_BAL")
    sex = st.selectbox("SEX", [1, 2])
    education = st.selectbox("EDUCATION", [1, 2, 3, 4])
    marriage = st.selectbox("MARRIAGE", [1, 2, 3])
    age = st.number_input("AGE", step=1)
    pay_sept = st.selectbox("PAY_SEPT", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_aug = st.selectbox("PAY_AUG", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_jul = st.selectbox("PAY_JUL", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_jun = st.selectbox("PAY_JUN", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_may = st.selectbox("PAY_MAY", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_apr = st.selectbox("PAY_APR", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    bill_amt_sept = st.number_input("BILL_AMT_SEPT")
    bill_amt_aug = st.number_input("BILL_AMT_AUG")
    bill_amt_jul = st.number_input("BILL_AMT_JUL")
    bill_amt_jun = st.number_input("BILL_AMT_JUN")
    bill_amt_may = st.number_input("BILL_AMT_MAY")
    bill_amt_apr = st.number_input("BILL_AMT_APR")
    pay_amt_sept = st.number_input("PAY_AMT_SEPT")
    pay_amt_aug = st.number_input("PAY_AMT_AUG")
    pay_amt_jul = st.number_input("PAY_AMT_JUL")
    pay_amt_jun = st.number_input("PAY_AMT_JUN")
    pay_amt_may = st.number_input("PAY_AMT_MAY")
    pay_amt_apr = st.number_input("PAY_AMT_APR")

    # Create a submit button
    submitted = st.form_submit_button("Predict")

    # Check if the form has been submitted
    if submitted:
        # Create a list to store the input values
        features = [
            limit_bal, sex, education, marriage, age,
            pay_sept, pay_aug, pay_jul, pay_jun, pay_may, pay_apr,
            bill_amt_sept, bill_amt_aug, bill_amt_jul, bill_amt_jun, bill_amt_may, bill_amt_apr,
            pay_amt_sept, pay_amt_aug, pay_amt_jul, pay_amt_jun, pay_amt_may, pay_amt_apr
        ]

        # Reshape features for prediction
        features_arr = np.array(features).reshape(1, -1)

        # Prediction
        prediction = model.predict(features_arr)
        default_payment = prediction[0]  # No need for tolist(), prediction is already a numpy array

        #Display prediction result
        result = "The credit card holder will default next month." if default_payment == 1 else "The credit card holder will not default next month."
        st.write(result)
