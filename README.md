# Employee Attrition Prediction and Analysis

This project focuses on predicting employee attrition using the IBM HR Analytics dataset. The pipeline includes data preprocessing, exploratory analysis, handling class imbalance, model training (Random Forest), and deploying a prediction tool using Streamlit.

---

## 📊 Dataset

- **Source**: [Kaggle - IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Features include**: employee age, job level, marital status, total working years, years at company, manager relationships, overtime, etc.

---

## 🔍 Project Workflow

### 1. Data Cleaning & Encoding
- Categorical columns were label encoded.
- Dropped uninformative or constant columns such as `EmployeeCount`, `StandardHours`, and `EmployeeNumber`.

### 2. Exploratory Data Analysis
- Countplots and pie charts were used for categorical analysis.
- Spearman correlation matrix was used to identify the most relevant features.

### 3. Handling Class Imbalance
- Applied **SMOTE** to oversample the minority class (Attrition = Yes).
- Ensured balanced training data for fair model performance.

### 4. Feature Selection
- Selected top 8 features with highest correlation to attrition:
  - `Age`
  - `JobLevel`
  - `MaritalStatus`
  - `OverTime`
  - `TotalWorkingYears`
  - `YearsAtCompany`
  - `YearsInCurrentRole`
  - `YearsWithCurrManager`

### 5. Model Training & Evaluation
- Trained and tested multiple models.
- **Final model used**: `RandomForestClassifier`
- Evaluated with:
  - Confusion Matrix
  - Classification Report
  - Accuracy, Precision, Recall, F1-Score

### 6. Deployment
- Deployed the final model using a **Streamlit app**.
- Users can input employee details and receive real-time attrition predictions.

---

## 🖥️ Streamlit App Inputs

The app accepts the following 8 inputs:

- Age
- Job Level
- Marital Status
- OverTime
- Total Working Years
- Years At Company
- Years In Current Role
- Years With Current Manager

---

## ✅ Results

- Achieved solid predictive performance using Random Forest.
- The deployed Streamlit app provides an interactive and easy-to-use interface for HR professionals to assess attrition risk based on real-time employee inputs.

---

You can try the live version of this app on Streamlit Cloud:  
👉 [Employee Attrition Prediction](https://employee-attrition-depi-project.streamlit.app/)
