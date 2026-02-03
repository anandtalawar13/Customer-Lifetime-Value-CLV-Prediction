# Customer Lifetime Value (CLV) Prediction

##  Project Overview
This project builds an **end-to-end Customer Lifetime Value (CLV) prediction system** using historical retail transaction data. The goal is to estimate a customer’s **6-month future value** to support **data-driven marketing, retention, and segmentation strategies**.

The solution combines **RFM-based feature engineering**, **advanced regression models**, **model explainability**, and a **Streamlit app** for real-time inference.

---

##  Business Problem
Customer acquisition is expensive. Businesses need to:
* Identify **high-value customers (VIPs)**
* Prioritize **retention and loyalty efforts**
* Optimize **marketing spend**

This project predicts CLV to enable **actionable customer segmentation** and revenue-focused decision-making.

---

### Key Fields

* `CustomerID`, `InvoiceDate`, `Quantity`, `UnitPrice`, `Country`
* Derived: `TotalPrice`, RFM metrics

---

## Data Cleaning & Preparation
* Removed transactions with missing `CustomerID`
* Excluded cancellations and returns (negative quantity/price)
* Converted timestamps to datetime
* Created transaction-level revenue (`TotalPrice`)
* Ensured leakage-safe time-based splitting

---
##  Exploratory Data Analysis (EDA)
Key insights from EDA:
* Heavy-tailed spending distribution (few customers drive most revenue)
* Seasonal revenue patterns
* High skew in monetary value → justified log transformation
* Correlation among RFM features → motivated regularization and tree models

EDA was performed **both before and after cleaning** to validate data quality and modeling assumptions.

---

##  Feature Engineering
Customer-level features were created using **RFM analysis** and behavioral metrics:
* **Recency** – Days since last purchase
* **Frequency** – Number of unique purchases
* **Monetary** – Total historical spend
* **AOV** – Average order value
* **Tenure** – Customer lifespan (days)
* **PurchaseInterval** – Avg. gap between purchases

---

##  Target Variable
* **6-month CLV** calculated using a time-based snapshot
* Modeled using `log1p(CLV)` to handle skew
* Predictions converted back to real monetary values for business use

---

##  Modeling Approach
Multiple regression models were trained and compared:
* Linear Regression
* Ridge & ElasticNet
* Random Forest
* **XGBoost (Final Model)**

### Why XGBoost?
* Captures non-linear customer behavior
* Handles feature interactions effectively
* Outperformed other models on RMSE and R²

**Final performance**:
* ~**40% R²** on held-out customers using transactional data only

---

##  Model Explainability (SHAP)

SHAP was used to interpret both **global** and **individual-level** predictions.

Key insights:
* **Purchase Frequency** and **Monetary Value** are the strongest CLV drivers
* Higher **Recency** (inactivity) negatively impacts future value
* SHAP enabled transparent explanations for VIP vs non-VIP customers

---

##  Customer Segmentation

Customers were segmented using **predicted CLV** (no leakage):
* **Low**
* **Medium**
* **High**
* **VIP**

Results showed a strong **Pareto effect**, where a small VIP segment contributed the majority of predicted revenue.

---

##  Streamlit Application

A Streamlit app was built to:
* Accept customer behavior inputs
* Predict 6-month CLV in real monetary terms
* Assign customer segments
* Provide business-friendly interpretations

---

##  Tech Stack
* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **XGBoost**
* **SHAP**
* **Streamlit**

---
