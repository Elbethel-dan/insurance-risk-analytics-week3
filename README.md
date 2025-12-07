# 📊 AlphaCare Insurance Solutions – Car Insurance Risk Analysis

Marketing Analytics Project (Task 1 & Task 2)

### 🏢 Business Objective

AlphaCare Insurance Solutions (ACIS) is committed to developing cutting-edge risk and predictive analytics for car insurance planning and marketing in South Africa.

You recently joined the data analytics team as a Marketing Analytics Engineer, and your first project is to analyse historical insurance claim data.

🎯 Project Goal

- The goal of this analysis is to:

- Identify low-risk customer segments

- Understand key drivers of high insurance claims

- Support premium optimisation strategies

- Help the marketing team attract new, low-risk clients by offering reduced premiums

To achieve this, the project focuses on:

- Exploratory Data Analysis (EDA)

- Data quality checks

- Risk segmentation

- Geographic, demographic, and vehicle-based trend analysis

- Setting up reproducible data pipelines

---

## ✅ Task 1 — Exploratory Data Analysis (EDA)

The first task focuses on exploring the dataset to uncover meaningful trends, understand data structure, and extract insights relevant to insurance risk.

🔍 What Was Done in EDA
### 1. Data Familiarization

Loaded and inspected the dataset

Reviewed column names, data types, and unique values

Defined the context for key variables (Premium, Claims, Vehicle Info, Geography, Cover Type)

### 2. Descriptive Analysis

Summary statistics for numerical features

Counts and distributions for categorical features

Identified outliers in variables such as TotalPremium and TotalClaims

Checked for inconsistencies or unusual patterns

### 3. Visualization & Insights

Created several insightful plots, including:

Geographical Trends

How premiums and claims differ across MainCrestaZone

Vehicle-Related Risk

Claim behaviour across different vehicle makes and models

Customer Segmentation Indicators

The relationship between cover type, premiums, and claims

---

## 📦 Task 2 — Data Version Control (DVC Setup)

DVC was introduced to ensure reproducibility, dataset version tracking, and clean separation between code and data.

🔧 Steps Completed
1. Initialize DVC
   ``` bash
     dvc init
   ```
2. Track the dataset with DVC
   ```
    dvc add data/MachinLearningRating_v3.txt
    ```
3. Commit DVC files
   ```
    git add insurance.csv.dvc .gitignore dvc.yaml
    git commit -m "Track raw insurance dataset with DVC"
   ```
