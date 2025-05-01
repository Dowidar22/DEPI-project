import streamlit as st
import joblib
import requests
import io
import numpy as np

st.set_page_config(page_title="Employee Attrition Prediction", layout="centered")
st.image("logo.png", width=900)
st.title("Employee Attrition Prediction")
st.write("Enter employee details to predict attrition:")

model_url = "https://github.com/ziad-samy/depi-project/raw/main/model.pkl"

try:
    response = requests.get(model_url)
    response.raise_for_status() 
    model = joblib.load(io.BytesIO(response.content))
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")

# 1. Input: Age
age = st.number_input("Age", min_value=18, max_value=65, value=24)

# 2. Input: Job Level
job_level = st.slider("Job Level (1-5)", min_value=1, max_value=5, value=1)

# 3. Input: Marital Status (encoded)
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"],index=1)
marital_status_encoded = {"Divorced": 0, "Married": 1, "Single": 2}[marital_status]

# 4. Input: OverTime (encoded)
overtime = st.selectbox("OverTime", ["No", "Yes"],index=0)
overtime_encoded = 1 if overtime == "Yes" else 0

# 5. Input: Total Working Years
total_working_years = st.number_input("Total Working Years", min_value=0, max_value=50, value=1)

# 6. Input: Years at company
years_at_company = st.number_input("Years At Company", min_value=0, max_value=40, value=1)

# 7. Input: Years in Current Role
years_in_current_role = st.number_input("Years in Current Role", min_value=0, max_value=40, value=0)

# 8. Input: Years With Current Manager
years_with_current_manager = st.number_input("Years With Current Manager", min_value=0, max_value=40, value=0)

# Prepare feature array
features = np.array([
    age, job_level, marital_status_encoded, overtime_encoded,
    total_working_years,years_at_company, years_in_current_role, years_with_current_manager
]).reshape(1, -1)

# Predict
if st.button("Predict Attrition"):
    try:
        prediction = model.predict(features)[0]
        result = "✅ Employee is likely to STAY ✅" if prediction == 0 else "⚠️ Employee is likely to LEAVE ⚠️"
        st.success(result)
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
