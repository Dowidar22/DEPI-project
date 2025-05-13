# Employee Attrition Prediction and Analysis – User Manual

---

## Table of Contents

1. [Introduction](#1-introduction)  
2. [Features Overview](#2-features-overview)  
3. [Installation & Setup](#3-installation--setup)  
4. [Using the Streamlit App](#4-using-the-streamlit-app)  
5. [Input Guide](#5-input-guide)  
6. [Understanding Results](#6-understanding-results)  
7. [Troubleshooting & FAQ](#7-troubleshooting--faq)  
8. [Project Structure](#8-project-structure)  
9. [Contribution Guidelines](#9-contribution-guidelines)  
10. [License & Credits](#10-license--credits)  
11. [Contact & Support](#11-contact--support)  

---

## 1. Introduction

Welcome to the Employee Attrition Prediction and Analysis project.  
This tool leverages machine learning to help HR professionals and analysts predict the likelihood of employee attrition (whether an employee will leave the company), using the IBM HR Analytics Attrition dataset. The solution includes data preprocessing, exploratory analysis, class imbalance handling, feature selection, model training, and a user-friendly web interface.

---

## 2. Features Overview

- Predicts employee attrition risk based on key HR factors.
- End-to-end pipeline: data processing, analysis, model training, and deployment.
- Uses Random Forest Classifier for robust, interpretable results.
- Streamlit web app for interactive, real-time predictions.
---

## 3. Installation & Setup

### Prerequisites

- Python 3.7+
- pip package manager

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Ziad-Samy/DEPI-project.git
   cd DEPI-project
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the IBM HR Analytics Dataset**
   - The project is based on the [IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).
   - **Important:** After downloading, you must edit the dataset path in your code or notebook to point to its local location on your machine.

---

## 4. Using the Streamlit App

1. **Start the Application**
   ```bash
   streamlit run app.py --server.port 8000 --server.address 0.0.0.0
   ```
   This command will launch the web app locally.

2. **Access the App**
   - After running the command, Streamlit will provide a local URL.
   - Open this URL in your browser:  
     [http://localhost:8000/](http://localhost:8000/)

3. **Live Demo**
   - You can also try the app online:  
     [Employee Attrition Prediction (Streamlit Cloud)](https://employee-attrition-depi-project.streamlit.app/)

---

## 5. Input Guide

The app requires the following employee details as input:

| Input Field               | Description                                    | Example          |
|--------------------------|------------------------------------------------|------------------|
| Age                      | Age of the employee                            | 29               |
| Job Level                | Level in company hierarchy (1-5)               | 2                |
| Marital Status           | Marital status (Single, Married, Divorced)     | Single           |
| OverTime                 | Works overtime? (Yes/No)                       | Yes              |
| Total Working Years      | Total years of professional experience         | 6                |
| Years At Company         | Number of years at current company             | 4                |
| Years In Current Role    | Years in current job role                      | 3                |
| Years With Current Manager | Years with current manager                    | 2                |

- Select or enter these details in the app’s interface.
- Click the "Predict" button to submit.

---

## 6. Understanding Results

- The app will display whether the employee is at risk of attrition.
- Results are based on the trained Random Forest model.
- Use these insights for proactive HR planning and intervention.

---

## 7. Troubleshooting & FAQ

**Q1: Streamlit app won’t start or gives a ModuleNotFoundError.**  
A: Ensure all dependencies are installed (`pip install -r requirements.txt`). Check that your Python version is compatible.

**Q2: Port already in use error.**  
A: Change the port by running:  
```bash
streamlit run app.py --server.port 8001
```

**Q3: I get a file or model not found error.**  
A: Make sure files like `model.pkl` are present in the project directory. Ensure your dataset path in code matches its location on your computer.

**Q4: How do I update dependencies?**  
A: Update `requirements.txt` and rerun `pip install -r requirements.txt`.

**Q5: Where can I get the dataset?**  
A: Download from Kaggle:  
[IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## 8. Project Structure

| File/Folder                | Purpose                                         |
|----------------------------|-------------------------------------------------|
| README.md                  | Project overview and workflow                   |
| app.py                     | Streamlit web application code                  |
| DEPI Project.ipynb         | Full data analysis and modeling notebook        |
| model.pkl                  | Trained Random Forest model                     |
| requirements.txt           | Python dependencies                             |
| startup.sh                 | Optional startup script                         |
| *.pdf                      | Project reports and documentation               |
| logo.png                   | Project logo                                    |

---

## 9. Contribution Guidelines

We welcome contributions! To contribute:

1. Fork the repository and create a new branch.
2. Make your changes with clear commit messages.
3. Submit a Pull Request describing your changes.
---

## 10. License & Credits

- **License:** This project is licensed under the MIT License. You are free to use, modify, and distribute this software for personal or commercial purposes, provided that you include the original copyright and license notice.
- The full license text can be found in the [LICENSE](LICENSE) file included with this repository.
- **Dataset:** IBM HR Analytics Attrition Dataset (Kaggle, [source](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)).
- **Libraries:** Streamlit, scikit-learn, pandas, numpy, imbalanced-learn, matplotlib, seaborn.
- **Team:** Developed by Ziad-Samy and contributors.


---

## 11. Contact & Support

- For issues and questions, open an [Issue on GitHub](https://github.com/Ziad-Samy/DEPI-project/issues).
- For direct contact:  
  GitHub: [Ziad-Samy](https://github.com/Ziad-Samy)  
  Email: *(ziadsami15@gmail.com)*

  GitHub: [Dowidar22](https://github.com/Dowidar22)  
  Email: *(mdowidar65@gmail.com)*
---
