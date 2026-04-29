# ❤️ Heart Disease Prediction using Machine Learning

This project uses machine learning to predict whether a person has **heart disease** based on clinical and health-related features.

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should **NOT** be used for real medical diagnosis.

---

## 📌 Objective

The objective of this project is to:

* Perform exploratory data analysis (EDA) on heart disease data
* Identify patterns related to heart disease
* Train and compare machine learning models
* Build a prediction system
* Deploy a simple **Streamlit web app** for user interaction

---

## 📊 Dataset

The dataset contains patient health information including:

* **age** – Age of the patient
* **sex** – Gender (0 = Female, 1 = Male)
* **cp** – Chest pain type
* **trestbps** – Resting blood pressure
* **chol** – Cholesterol level
* **fbs** – Fasting blood sugar
* **restecg** – Resting ECG results
* **thalach** – Maximum heart rate achieved
* **exang** – Exercise-induced angina
* **oldpeak** – ST depression
* **slope** – Slope of peak exercise
* **ca** – Number of major vessels
* **thal** – Thalassemia
* **target** – Heart disease presence (1 = Yes, 0 = No)

---

## ⚙️ Project Workflow

1. Data loading
2. Exploratory Data Analysis (EDA)
3. Feature engineering and preprocessing
4. Train-test split (with stratification)
5. Feature scaling using StandardScaler
6. Model training:

   * Logistic Regression
   * Random Forest
   * Support Vector Machine (SVM)
7. Model evaluation
8. Model comparison
9. Final model selection
10. Model saving
11. Streamlit app development

---

## 🧠 Models Used

* **Logistic Regression**
* **Random Forest Classifier**
* **Support Vector Machine (SVM) – Final Model**

---

## 📈 Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🏆 Results

* SVM achieved the best performance
* Final model achieved approximately:

---

## 💡 Key Insights

* Age, chest pain type, and maximum heart rate are important features
* Exercise-induced angina and ST depression show strong patterns
* Feature scaling is essential for SVM performance

---

## 💾 Model Saving

The trained model and scaler are saved for deployment:

---

## 🖥️ Streamlit App

An interactive web app was built using Streamlit.

### Features:

* User inputs patient details
* Model predicts heart disease presence
* Instant result display




