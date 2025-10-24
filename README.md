# Rain Prediction Project

This project predicts whether it will rain tomorrow in major US cities using weather data and machine learning. It includes an end-to-end workflow from data preprocessing, modeling, to a user-friendly web app for instant predictions.

---

## 🗃 Project Structure

- **usa_rain_prediction_dataset_2024_2025.csv** — Raw weather data
- **rain_prediction_model.pkl** — Trained ML model (BernoulliNB, tuned with GridSearchCV)
- **app.py** — Streamlit web application for predictions
- **README.md** — Documentation and instructions

---

## 📊 Data Preparation & Feature Engineering

- **Dataset Columns:**  
  - Date
  - Location (city)
  - Temperature
  - Humidity
  - Wind Speed
  - Precipitation
  - Cloud Cover
  - Pressure
  - Rain Tomorrow (target, 1=rain, 0=no rain)

- **Steps:**  
  - Downsampled to balance classes for `Rain Tomorrow`.
  - Extracted `Year`, `Month`, `Day` from the Date.
  - Encoded `Location` with LabelEncoder for ML compatibility.
  - Applied cube root transformation to Precipitation for better distribution.

---

## 🏋️‍♂️ Model Training

- Used both `RandomForestClassifier` and `BernoulliNB` from scikit-learn.
- Performed hyperparameter tuning on BernoulliNB (via GridSearchCV).
- Evaluated with accuracy, confusion matrix, classification report.
- Saved best performing model (`rain_prediction_model.pkl`) for use in the app.

---

## 🌐 Web App Features

Built using **Streamlit**:
- **Calendar picker** for date input.
- **Dropdown menu** for city selection.
- **Manual entry** for weather variables.
- Applies all preprocessing (encoding, transformations) to user input.
- Returns an instant prediction: will it rain tomorrow (`Yes/No`)?

---

## 🚀 Running the Project

### Prerequisites


### To Run the App

1. Place `app.py` and `rain_prediction_model.pkl` in the same folder.
2. Run in terminal:
    ```
    streamlit run app.py
    ```
3. Open the browser page that appears and use the interface.

---

## 🔁 Git Usage Tips

To push your branch for the first time, use:
