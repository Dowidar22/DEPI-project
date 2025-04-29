# Employee Attrition Prediction and Analysis

This project analyzes and predicts employee attrition using the IBM HR Analytics dataset. It includes data preprocessing, exploratory analysis, machine learning modeling, and deployment through a Streamlit application.

## 📊 Dataset

- Source: [Kaggle - IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
-  Features include: age, gender, job role, department, overtime, education, distance from home, monthly income, etc.

## 🔍 Project Workflow

1. **Data Cleaning & Encoding**

   - Replaced categorical values with numeric or one-hot encoded them.
   - Dropped uninformative columns (e.g., EmployeeCount, StandardHours).

2. **Exploratory Data Analysis**

   - Countplots and pie charts for categorical variables.
   - Correlation matrix using Spearman correlation.

3. **Handling Imbalance**

   - SMOTE was used to balance the target (Attrition).

4. **Model Training & Evaluation**

   - Trained multiple models:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - Gradient Boosting
   - Evaluated using:
     - Confusion Matrix
     - Classification Report
     - Accuracy, Precision, Recall, F1 Score

5. **Deployment**

   - Built a Streamlit dashboard to predict attrition based on user input.

## ✅ Results

- Successfully predicted attrition with good performance using ensemble models.
- Streamlit app visualizes inputs, predictions.
