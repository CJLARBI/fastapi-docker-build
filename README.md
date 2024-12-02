

The provided data is a modified version of a publicly available data source, and is subject to copyright.


### Sepsis Prediction API
This project implements a Machine Learning (ML) API designed to predict whether a patient in the ICU is at risk of developing sepsis. The API is built with a focus on scalability and performance, leveraging Docker for containerization and ease of deployment.

### Table of Contents
Introduction
Features
Dataset Overview
Technologies Used
License

### Introduction
Sepsis is a life-threatening condition that arises when the body's response to infection causes injury to its tissues and organs. Early prediction of sepsis is crucial in providing timely interventions and improving patient outcomes. This project provides a robust Machine Learning-based API for sepsis prediction using patient medical data.

### Features
Predict sepsis risk based on patient medical records.
Scalable and containerized application using Docker.
RESTful API endpoints for integration with healthcare systems or applications.
Accurate predictions powered by pre-trained machine learning models.

### Dataset Overview
The dataset used for this project contains medical records of patients admitted to the ICU. The primary goal is to predict the Sepssis target variable, which indicates whether a patient is likely to develop sepsis.

### Column Name	Attribute/Target	Description
ID	N/A	Unique number to represent patient ID
PRG	Attribute 1	Plasma glucose
PL	Attribute 2	Blood Work Result-1 (mu U/ml)
PR	Attribute 3	Blood Pressure (mm Hg)
SK	Attribute 4	Blood Work Result-2 (mm)
TS	Attribute 5	Blood Work Result-3 (mu U/ml)
M11	Attribute 6	Body Mass Index (BMI): weight in kg/(height in m)^2
BD2	Attribute 7	Blood Work Result-4 (mu U/ml)
Age	Attribute 8	Patient's age (years)
Insurance	N/A	Indicates if a patient holds a valid insurance card

### Hypotheses:
 Hyp 1: Patients with higher PL are more likely to test Positive for sepsis compared to those with lower PL.
 Hyp 2: Patients without insurance are more likely to test positive for sepsis compared to those with insurance.
 Hyp 3: Is there a statistically significant difference in the PL values between patients with positive sepsis and those with negative sepsis?

### Business Questions:
Question 1:
Is there a relationship between patients' age and the outcome of Sepssis?

Question 2:
Does insurance status impact the relationship between age and sepsis outcomes?

Question 3:
What is the distribution of BMI (M11) for Positive and Negative Sepsis outcomes?

Question 4:
How does the number of pregnancies (PRG) vary between Positive and Negative Sepsis outcomes?

Question 5: How does the number of live births (PL) vary between Positive and Negative Sepsis outcomes?

### Sepssis	Target	Positive:
Patient in ICU will develop sepsis; Negative: Otherwise
### Technologies Used:
Python: For building the machine learning model and API.
FastAPI: To develop the RESTful API.
Scikit-learn: For machine learning model development.
Docker: For containerization and deployment.
NumPy and Pandas: For data processing and analysis.

### Donor of database: 
                          The Johns Hopkins University
                          Johns Hopkins Road
                          Laurel, MD 20707
                          (301) 953-6231

### License
This project is licensed under the MIT License. See the LICENSE file for details.