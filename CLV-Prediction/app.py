import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load Model & Features
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("clv_xgboost_model.pkl")
    features = joblib.load("clv_model_features.pkl")
    return model, features

model, model_features = load_model()

# -----------------------------
# App UI
# -----------------------------
st.set_page_config(page_title="CLV Prediction App", layout="centered")

st.title("ustomer Lifetime Value (CLV) Predictor")
st.write("Predict **6-month CLV** and customer segment using an XGBoost model.")

st.divider()

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("Customer Behavior Inputs")

recency = st.number_input("Recency (days since last purchase)", min_value=0, value=30)
frequency = st.number_input("Purchase Frequency", min_value=1, value=5)
monetary = st.number_input("Total Monetary Value", min_value=0.0, value=2000.0)
aov = st.number_input("Average Order Value", min_value=0.0, value=400.0)
tenure = st.number_input("Customer Tenure (days)", min_value=0, value=180)
purchase_interval = st.number_input("Purchase Interval (days)", min_value=1, value=30)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict CLV"):
    input_data = pd.DataFrame([{
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary,
        "AOV": aov,
        "Tenure": tenure,
        "PurchaseInterval": purchase_interval
    }])

    # Ensure feature order
    input_data = input_data[model_features]

    # Predict (log scale)
    clv_log = model.predict(input_data)

    # Convert back to real CLV
    clv_real = np.expm1(clv_log)[0]

    # Segment logic
    if clv_real <= 0:
        segment = "Low"
    elif clv_real < 1000:
        segment = "Medium"
    elif clv_real < 5000:
        segment = "High"
    else:
        segment = "VIP"

    # -----------------------------
    # Output
    # -----------------------------
    st.success("Prediction Complete")

    st.metric("Predicted 6-Month CLV", f"{clv_real:,.2f}")
    st.metric("Customer Segment", segment)

    st.divider()

    st.write("### Business Interpretation")
    if segment == "VIP":
        st.write("**VIP Customer** – prioritize retention & premium offers.")
    elif segment == "High":
        st.write("**High Value Customer** – upsell & loyalty programs recommended.")
    elif segment == "Medium":
        st.write("**Medium Value Customer** – nurture with targeted campaigns.")
    else:
        st.write("*Low Value Customer** – automate engagement or reactivation offers.")
