# import streamlit as st
# import pandas as pd
# import joblib

# # Load the trained model and column structure
# model = joblib.load('churn_model.pkl')
# model_columns = joblib.load('model_columns.pkl')

# st.title("Customer Churn Prediction")
# st.write("Enter customer details to predict churn probability.")

# # Input fields
# tenure = st.slider("Tenure (months)", 0, 72, 12)

# monthly_charges_inr = st.number_input("Monthly Charges (₹)", 0.0, 15000.0, 5000.0)
# total_charges_inr = st.number_input("Total Charges (₹)", 0.0, 750000.0, 75000.0)

# # Convert to USD internally, since the model was trained on USD-scale values
# USD_TO_INR = 83
# monthly_charges = monthly_charges_inr / USD_TO_INR
# total_charges = total_charges_inr / USD_TO_INR

# contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
# internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
# payment_method = st.selectbox(
#     "Payment Method",
#     ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
# )

# operator = st.selectbox("Telecom Operator", ["Airtel", "Jio", "Vi", "BSNL"])
# st.caption(
#     "ℹ️ This model predicts churn based on account behavior (tenure, contract, billing) — "
#     "patterns that apply across operators. The operator selection shows this model can be "
#     "deployed for any telecom provider's customer base."
# )
# st.caption("💡 Charges are entered in ₹ and converted internally to match the model's training currency (USD).")

# # Build input dataframe matching training format
# # NOTE: operator is intentionally NOT included here — see caption above
# input_dict = {
#     'tenure': tenure,
#     'MonthlyCharges': monthly_charges,
#     'TotalCharges': total_charges,
#     'Contract_One year': 1 if contract == "One year" else 0,
#     'Contract_Two year': 1 if contract == "Two year" else 0,
#     'InternetService_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
#     'InternetService_No': 1 if internet_service == "No" else 0,
#     'PaymentMethod_Credit card (automatic)': 1 if payment_method == "Credit card (automatic)" else 0,
#     'PaymentMethod_Electronic check': 1 if payment_method == "Electronic check" else 0,
#     'PaymentMethod_Mailed check': 1 if payment_method == "Mailed check" else 0,
# }

# input_df = pd.DataFrame([input_dict])

# # Add any missing columns the model expects, filled with 0
# for col in model_columns:
#     if col not in input_df.columns:
#         input_df[col] = 0

# input_df = input_df[model_columns]  # reorder to match training

# if st.button("Predict"):
#     prediction = model.predict(input_df)[0]
#     probability = model.predict_proba(input_df)[0][1]

#     if prediction == 1:
#         st.error(f"⚠️ High risk of churn — Probability: {probability:.2%}")
#     else:
#         st.success(f"✅ Likely to stay — Churn Probability: {probability:.2%}")


import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📡",
    layout="centered"
)

# Load the trained model and column structure
model = joblib.load('churn_model.pkl')
model_columns = joblib.load('model_columns.pkl')

# ---------- HEADER ----------
st.markdown(
    """
    <div style="text-align:center; padding: 10px 0 20px 0;">
        <h1>📡 Customer Churn Prediction</h1>
        <p style="color:gray; font-size:16px;">
            Predict whether a telecom customer is likely to stay or leave, based on account behavior.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- SIDEBAR INPUTS ----------
st.sidebar.header("🧾 Customer Details")

tenure = st.sidebar.slider("📅 Tenure (months)", 0, 72, 12)

st.sidebar.subheader("💰 Billing")
monthly_charges_inr = st.sidebar.number_input("Monthly Charges (₹)", 0.0, 15000.0, 5000.0)
total_charges_inr = st.sidebar.number_input("Total Charges (₹)", 0.0, 750000.0, 75000.0)

USD_TO_INR = 83
monthly_charges = monthly_charges_inr / USD_TO_INR
total_charges = total_charges_inr / USD_TO_INR

st.sidebar.subheader("📄 Account")
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

st.sidebar.subheader("📶 Operator")
operator = st.sidebar.selectbox("Telecom Operator", ["Airtel", "Jio", "Vi", "BSNL"])
st.sidebar.caption(
    "This field is for display only. The model predicts churn using account behavior "
    "(tenure, contract, billing) — patterns that apply across any operator."
)

predict_btn = st.sidebar.button("🔮 Predict Churn", use_container_width=True)

# ---------- MAIN PANEL: SUMMARY CARD ----------
col1, col2, col3 = st.columns(3)
col1.metric("Tenure", f"{tenure} mo")
col2.metric("Monthly Bill", f"₹{monthly_charges_inr:,.0f}")
col3.metric("Contract", contract)

st.divider()

# Build input dataframe matching training format
input_dict = {
    'tenure': tenure,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'Contract_One year': 1 if contract == "One year" else 0,
    'Contract_Two year': 1 if contract == "Two year" else 0,
    'InternetService_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
    'InternetService_No': 1 if internet_service == "No" else 0,
    'PaymentMethod_Credit card (automatic)': 1 if payment_method == "Credit card (automatic)" else 0,
    'PaymentMethod_Electronic check': 1 if payment_method == "Electronic check" else 0,
    'PaymentMethod_Mailed check': 1 if payment_method == "Mailed check" else 0,
}

input_df = pd.DataFrame([input_dict])

for col in model_columns:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model_columns]

# ---------- RESULT ----------
if predict_btn:
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Churn")
    else:
        st.success(f"✅ Likely to Stay")

    st.write(f"**Churn Probability: {probability:.1%}**")
    st.progress(float(probability))

    with st.expander("ℹ️ How to read this"):
        st.write(
            "This probability reflects how closely this customer's profile matches "
            "patterns of customers who left in the training data. Higher tenure and "
            "longer contracts typically lower churn risk; month-to-month contracts and "
            "high monthly charges typically raise it."
        )
else:
    st.info("👈 Fill in the customer details in the sidebar and click **Predict Churn**.")

st.caption("💡 Charges are entered in ₹ and converted internally to match the model's training currency (USD).")