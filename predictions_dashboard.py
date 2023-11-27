import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def load_data():
    lstm = pd.read_csv('lstm_predictions.csv')
    arima = pd.read_csv('arima_prediction.csv')
    actual = pd.read_csv('actual_y.csv')
    return lstm, arima, actual

lstm, arima, actual = load_data()

st.title('LSTM and ARIMA models versus Actual')
st.write('this doashboard is to show the difference between the lstm and arima model and how accurate they are at predicting crime in 2016')


