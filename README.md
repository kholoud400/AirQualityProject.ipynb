# AirQualityProject.ipynb
#  Air Quality Index (AQI) Prediction

This project focuses on predicting the Air Quality Index (AQI) using environmental pollutant data. Multiple machine learning models were trained and evaluated to identify the best-performing model for accurate AQI prediction.

---

##  Problem Statement

Air pollution is a major environmental issue that affects human health and quality of life.

The goal of this project is to predict the Air Quality Index (AQI) based on different pollutant measurements such as PM2.5, PM10, NO2, CO, SO2, and others.

---

##  Dataset

The dataset contains daily air quality measurements collected from multiple cities.

### Features:
- PM2.5, PM10
- NO, NO2, NOx
- CO, SO2, O3
- Benzene, Toluene, Xylene
- City, Date

### Target:
- AQI (Air Quality Index)

Source: (add dataset link here)

---

##  Data Preprocessing

- Handled missing values using median (numerical) and most frequent (categorical)
- Converted `Date` column into:
  - Year
  - Month
- Applied One-Hot Encoding for categorical variable (City)
- Built preprocessing pipeline using `ColumnTransformer`

---

##  Machine Learning Models

The following regression models were trained and compared:

- Linear Regression
- Ridge & Lasso Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Regressor
- Random Forest
- Extra Trees
- Bagging Regressor
- Gradient Boosting
- HistGradientBoosting
- XGBoost
- LightGBM
- CatBoost
- Support Vector Regressor (SVR)

---

##  Best Model

- **Model Used:** LightGBM Regressor  
- **Performance:**
  - R² Score: ~0.91  
  - MAE: ~20.95  
  - RMSE: ~40.11  

LightGBM achieved the best performance among all tested models.

---

##  Key Insights

The most important features affecting AQI were:

- PM10
- CO
- PM2.5
- NO2
- SO2

---

##  Model Saving

The final trained model was saved using `joblib`:

```python
joblib.dump(best_model, "aqi_best_model.pkl")


## Dataset and Model

Due to file size limitations, the dataset and trained model are hosted on Google Drive.

Dataset: [https://drive.google.com/drive/folders/1QI09-6AX2GUJMclS_QRlQ-bN0QBfrVfR]

Trained Model: [https://drive.google.com/drive/folders/1QI09-6AX2GUJMclS_QRlQ-bN0QBfrVfR]
## Google drive link : [https://drive.google.com/drive/folders/1QI09-6AX2GUJMclS_QRlQ-bN0QBfrVfR]
