# 📊 AlphaCare Insurance Solutions – Car Insurance Risk Analysis

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
---

## 📊 Task 3 — Statistical Hypothesis Testing

This task focuses on statistically validating assumptions about key insurance risk drivers. These insights will guide the development of an effective segmentation strategy.

### 🎯 Goal

Test whether differences in claims, premiums, and risk metrics across customer groups are statistically significant.

Confirm or reject business hypotheses that drive pricing and marketing decisions.

### 🔍 What Was Done
1. Formulated Clear Null (H₀) and Alternative (H₁) Hypotheses

Hypotheses tested include:

#### Geographic Risk

H₀: There are no risk differences across provinces.

H₁: At least one province shows significantly different risk.

#### Zip-Code Risk

H₀: There are no risk differences between zip codes.

H₁: Some zip codes exhibit higher or lower risk.

#### Margin Differences

H₀: There is no significant difference in profit margin between zip codes.

H₁: Profit margin varies significantly across zip codes.

#### Gender Risk

H₀: There is no significant risk difference between women and men.

H₁: Gender groups show different levels of risk exposure or claim patterns.

2. Applied Appropriate Statistical Tests

Depending on the variable type and distribution:

Chi-square tests → for categorical variables (Gender, Marital Status, Claim Frequency).

ANOVA → for comparing risk across multiple groups (Provinces, Zip Codes).

T-tests / Z-tests → for comparing mean differences (Margins, Premiums, Severity).

3. Interpreted Test Results

Checked p-values against significance level (α = 0.05).

Rejected or failed to reject H₀ based on evidence.

Summarized practical implications for segmentation strategy.


---

## 🤖 Task 4 — Predictive Modelling for Dynamic Risk-Based Pricing

The goal of Task 4 is to develop machine learning models that can predict insurance risk and support real-time premium optimisation.

#### Model Development

Built and compared multiple models:

Logistic Regression → for classifying claim likelihood

Random Forest → for both classification and regression

Gradient Boosting Models (XGBoost / LightGBM) → for superior predictive power

Linear Models → for claim severity analysis
