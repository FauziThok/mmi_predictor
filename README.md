# Earthquake MMI Prediction

A Machine Learning project that predicts the **Modified Mercalli Intensity (MMI)** of earthquakes using physical seismic parameters. Built using a **Random Forest Classifier** and deployed through a **Streamlit web app**.

---

## Project Summary

This project aims to provide a fast, automated estimation of earthquake impact by predicting the MMI level based on key seismic features. MMI is classified into three categories:

* **Low (≤ 3)**
* **Medium (4–6)**
* **High (≥ 7)**

The model is trained using labeled seismic data and achieves strong performance across all classes.

---

## Key Features

* **Input Parameters:**
  Magnitude, Depth, Distance, Latitude, Longitude

* **Task:**
  Multiclass classification of MMI levels (Low, Medium, High)

* **Model:**
  Random Forest Classifier

* **Performance:**
  **93.4% Overall Accuracy**

* **Deployment:**
  Fully interactive **Streamlit App** for real-time predictions

---

## Potential Use Cases

* Early estimation for earthquake impact analysis
* Rapid decision support for emergency response
* Educational demonstrations of seismic intensity prediction

---

## Get Started

### 1. Clone the repository

```bash
git clone https://github.com/your/repository.git
cd repository
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pandas scikit-learn
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

---

## Model Performance Snapshot

| Class  | Precision | Recall | F1-Score |
| ------ | --------- | ------ | -------- |
| High   | 0.94      | 0.68   | 0.79     |
| Low    | 0.92      | 0.96   | 0.94     |
| Medium | 0.94      | 0.97   | 0.95     |

---

## 🔗 Links

* **GitHub Repository:** *[https://github.com/FauziThok/mmi_predictor.git]*
* **Live Streamlit App:** *[https://mmipredictor-3s25fy3b7qmk27mjhpunee.streamlit.app/]*

---

Feel free to improve, extend, or integrate the model into larger seismic analysis systems!
