## Running the Streamlit Application

This project includes a **Streamlit web application** that allows users to predict **6-month Customer Lifetime Value (CLV)** and view model explainability usPython **+**
* pip installed

---

### Install Dependencies

From the project root directory, run:

```bash
pip install -r requirements.txt
```

---

### Run the Streamlit App Locally

Execute the following command from the same directory where `app.py` exists:

```bash
python -m streamlit run app.py
```

After running the command:

* Streamlit will start a local server
* Open the provided URL (ally `http://localhost:8501`) in your browser

---

## Application Features

* Input customer behavior metrics:

  * Recency
  * Frequency
  * Monetary value
  * Average Order Value (AOV)
  * Tenure
  * Purchase Interval
* Predict **6-month CLV**
* Automatically assign **CLV segment** (Low / Medium / High)
* play **SHAP-based explainability** for individual predictions

---
### Notes

* The model predicts **log-transformed CLV** internally and converts predictions back to real monetary values for busin interpretation.
* SHAP values are computed dynamically to explain each prediction.

---

### Troubleshooting

* Ensure `clv_xgboost_model.pkl`,`clv_model_features.pkl` are in the **same directory** as `app.py`
* Error related to xgboost installation use `python -m pip install xgboost`
* If Streamlit fails to start, verify a dependencies are installed correctly
* For deployment issues, check logs inStreamlit Cloud

---