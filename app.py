import streamlit as st
import joblib
import requests
import io

st.set_page_config(page_title="Employee Attrition Prediction", layout="centered")

st.title("Employee Attrition Prediction")
st.write("Fill in the employee details to predict attrition.")

model_url = "https://github.com/ziad-samy/depi-project/raw/main/gb.pkl"

try:
    response = requests.get(model_url)
    response.raise_for_status() 
    model = joblib.load(io.BytesIO(response.content))
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")


# Define feature inputs
age = st.number_input("Age", min_value=18, max_value=65, value=30)
business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
daily_rate = st.number_input("Daily Rate", min_value=100, max_value=1500, value=800)
department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
distance_from_home = st.number_input("Distance From Home (km)", min_value=0, max_value=100, value=10)
education = st.slider("Education Level (1-5)", min_value=1, max_value=5, value=3)
education_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Other"])
environment_satisfaction = st.slider("Environment Satisfaction (1-4)", min_value=1, max_value=4, value=3)
gender = st.selectbox("Gender", ["Male", "Female"])
hourly_rate = st.number_input("Hourly Rate", min_value=10, max_value=100, value=50)
job_involvement = st.slider("Job Involvement (1-4)", min_value=1, max_value=4, value=3)
job_level = st.slider("Job Level (1-5)", min_value=1, max_value=5, value=2)
job_role = st.selectbox("Job Role", ["Manager", "Sales Executive", "Research Scientist", "Lab Technician", "HR", "Other"])
job_satisfaction = st.slider("Job Satisfaction (1-4)", min_value=1, max_value=4, value=3)
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
monthly_rate = st.number_input("Monthly Rate ($)", min_value=1000, max_value=50000, value=5000)
num_companies_worked = st.number_input("Number of Companies Worked", min_value=0, max_value=10, value=3)
overtime = st.selectbox("OverTime", ["Yes", "No"])
percent_salary_hike = st.slider("Percent Salary Hike", min_value=0, max_value=50, value=10)
performance_rating = st.slider("Performance Rating (1-5)", min_value=1, max_value=5, value=3)
relationship_satisfaction = st.slider("Relationship Satisfaction (1-4)", min_value=1, max_value=4, value=3)
stock_option_level = st.slider("Stock Option Level (0-3)", min_value=0, max_value=3, value=1)
total_working_years = st.number_input("Total Working Years", min_value=0, max_value=50, value=10)
training_times_last_year = st.slider("Training Times Last Year", min_value=0, max_value=10, value=2)
work_life_balance = st.slider("Work-Life Balance (1-4)", min_value=1, max_value=4, value=3)
years_at_company = st.number_input("Years At Company", min_value=0, max_value=40, value=5)
years_since_last_promotion = st.number_input("Years Since Last Promotion", min_value=0, max_value=20, value=2)

# Encoding categorical features
business_travel_encoded = {"Non-Travel": 0, "Travel_Rarely": 1, "Travel_Frequently": 2}[business_travel]
education_field_encoded = {"Life Sciences": 0, "Medical": 1, "Marketing": 2, "Technical Degree": 3, "Other": 4}[education_field]
gender_encoded = 1 if gender == "Male" else 0
department_encoded = {"Human Resources": 0, "Research & Development": 1, "Sales": 2}[department]
job_role_encoded = {"Manager": 0, "Sales Executive": 1, "Research Scientist": 2, "Lab Technician": 3, "HR": 4, "Other": 5}[job_role]
marital_status_encoded = {"Single": 0, "Married": 1, "Divorced": 2}[marital_status]
overtime_encoded = 1 if overtime == "Yes" else 0

# Prepare input features
features = np.array([
    age, business_travel_encoded, daily_rate, department_encoded, distance_from_home,
    education, education_field_encoded, environment_satisfaction, gender_encoded,
    hourly_rate, job_involvement, job_level, job_role_encoded,
    job_satisfaction, marital_status_encoded, monthly_rate, num_companies_worked,
    overtime_encoded, percent_salary_hike, performance_rating,
    relationship_satisfaction, stock_option_level, total_working_years,
    training_times_last_year, work_life_balance, years_since_last_promotion,years_at_company 
]).reshape(1, -1)

# Prediction
if st.button("Predict Attrition"):
    try:
        prediction = model.predict(features)[0]
        result = "✅✅ Employee is likely to STAY ✅✅" if prediction == 0 else "⚠️⚠️ Employee is likely to LEAVE ⚠️⚠️"
        st.success(result)
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
