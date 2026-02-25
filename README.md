# 🎯 Job Acceptance Prediction System

## 📌 Overview
The Job Acceptance Prediction System is an end-to-end Machine Learning project designed to help recruitment teams predict whether a candidate will accept or reject a job offer.  
The system analyzes candidate academic performance, skills, experience, interview outcomes, and market factors to generate insights and predictive outcomes.

This project demonstrates the full data science workflow including data cleaning, exploratory analysis, feature engineering, model training, evaluation, and dashboard visualization.

---

## 🎯 Problem Statement
Recruitment teams often face offer dropouts even after selecting suitable candidates.  
This leads to increased hiring time, operational delays, and additional recruitment costs.

This project aims to:
- Predict job acceptance probability
- Identify key drivers influencing placement decisions
- Handle real-world messy recruitment data
- Provide actionable insights for HR decision-making

---

## 🧠 Project Workflow

1. Data Collection  
2. Data Cleaning & Preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering  
5. Machine Learning Modeling  
6. Model Evaluation  
7. Dashboard Visualization  

---

## 📊 Dataset Information
- Dataset Size: ~50,000 candidate records  
- Domain: HR Recruitment & Placement Analytics  
- Target Variable: **status**
  - Placed → 1
  - Not Placed → 0  

Features include:
- Academic scores
- Skills match percentage
- Relevant experience
- Interview scores
- Company tier
- Competition level
- Candidate preferences

---

## ⚙️ Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Streamlit
- SQL (optional)
- VS Code

---

## 🤖 Machine Learning Models

### Baseline Model
- Logistic Regression

### Final Model
- Random Forest Classifier

**Why Random Forest?**
- Handles non-linear relationships
- High prediction accuracy
- Reduces overfitting
- Provides feature importance insights

---

## 📈 Key Insights from EDA

- Higher skills match significantly improves placement probability
- Company tier strongly influences acceptance rates
- Moderate experience candidates show better placement success
- Interview performance is a major predictor
- Higher competition reduces acceptance probability

---

## 📊 Streamlit Dashboard KPIs

- Total Candidates
- Placement Rate (%)
- Job Acceptance Rate (%)
- Average Interview Score
- Average Skills Match %
- Offer Dropout Rate
- High-Risk Candidate Percentage

---

## 📂 Project Structure

