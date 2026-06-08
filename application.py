import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

# =========================
# Load Data + Model
# =========================
df = pd.read_csv("city_day.csv")
df["Date"] = pd.to_datetime(df["Date"])

model = joblib.load("aqi_best_model.pkl")

# =========================
# Title
# =========================
st.title("🌍 Air Quality Index (AQI) Dashboard & Prediction")

# =========================
# Sidebar Navigation
# =========================
page = st.sidebar.radio("Choose Section", ["📊 Dashboard", "🤖 Prediction"])

# =========================
# DASHBOARD
# =========================
if page == "📊 Dashboard":

    st.header("Air Quality Analysis")

    # Filters
    city = st.selectbox("Select City", df["City"].unique())

    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    # Filter data
    mask = (
        (df["City"] == city) &
        (df["Date"] >= pd.to_datetime(start_date)) &
        (df["Date"] <= pd.to_datetime(end_date))
    )

    city_df = df[mask]

    st.subheader("📈 AQI Trend")
    fig, ax = plt.subplots()
    ax.plot(city_df["Date"], city_df["AQI"])
    ax.set_xlabel("Date")
    ax.set_ylabel("AQI")
    st.pyplot(fig)

    # Pollutants
    st.subheader("☁️ Average Pollutants")

    pollutants = ["PM2.5","PM10","NO","NO2","NOx","CO","SO2","O3"]
    avg_vals = city_df[pollutants].mean()

    st.bar_chart(avg_vals)

    # AQI distribution
    st.subheader("🏷️ AQI Levels")

    def bucket(aqi):
        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Moderate"
        elif aqi <= 200:
            return "Poor"
        else:
            return "Very Poor"

    city_df["AQI_Bucket"] = city_df["AQI"].apply(bucket)

    st.bar_chart(city_df["AQI_Bucket"].value_counts())


# =========================
# PREDICTION PAGE
# =========================
elif page == "🤖 Prediction":

    st.header("Predict AQI")

    city = st.selectbox("City", df["City"].unique())

    pm25 = st.number_input("PM2.5")
    pm10 = st.number_input("PM10")
    no = st.number_input("NO")
    no2 = st.number_input("NO2")
    nox = st.number_input("NOx")
    co = st.number_input("CO")
    so2 = st.number_input("SO2")
    o3 = st.number_input("O3")

    input_data = pd.DataFrame([[pm25, pm10, no, no2, nox, co, so2, o3]],
                              columns=["PM2.5","PM10","NO","NO2","NOx","CO","SO2","O3"])

    if st.button("Predict AQI"):

        prediction = model.predict(input_data)[0]

        st.success(f"🌡️ Predicted AQI: {prediction}")

        # bucket
        if prediction <= 50:
            st.info("Good 😊")
        elif prediction <= 100:
            st.warning("Moderate 😐")
        elif prediction <= 200:
            st.error("Poor 😷")
        else:
            st.error("Very Poor ☠️")