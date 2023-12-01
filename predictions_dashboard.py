import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def load_data():
    lstm = pd.read_csv('lstm_predictions.csv')
    arima = pd.read_csv('arima_prediction.csv')
    actual = pd.read_csv('actual_y.csv')
    return lstm, arima, actual
#GEtting the data stored in these variables. I cahced it above so the dashboard is not slow
lstm, arima, actual = load_data()
lstm['Type'] = 'LSTM'
arima['Type'] = 'ARIMA'
actual['Type'] = 'ACTUAL'
df = pd.concat([lstm, arima, actual])

st.title('LSTM and ARIMA models versus Actual')
st.write('this doashboard is to show the difference between the lstm and arima model and how accurate they are at predicting crime in 2016')
geoid = actual['geodi10'].unique().tolist()
geoid = ['All'] + geoid
#Sidebar options to then change the graphs
areas = st.sidebar.multiselect('Choose the areas you would like to include',geoid)
#aggregating badsed on geoid options

if areas == ['All']:
    actual_counts = df.groupby(['Type', 'Quarter']).sum()
    actual_counts = actual_counts.reset_index()
else:
    actual_counts = df[df['geodi10'].isin(areas)]
    actual_counts = df.groupby(['Type', 'Quarter']).sum()
    actual_counts = actual_counts.reset_index()
#Making graphs 
tab1, tab2, tab3 = st.tabs(["All Other Theft", "Simple Assualt", "Theft From Motor Vehicle"])
with tab1:
    Alltheft_line = alt.Chart(actual_counts[['Type', 'Quarter', 'All Other Thefts']]).mark_line().transform_fold(fold=df['Type'].unique().tolist(), as_=['variable', 'value']).encode(
        x='Quarter',
        y='All Other Thefts',
        color='Type'
    )
    st.altair_chart(Alltheft_line, use_container_width=True)
with tab2:
    assault_line = alt.Chart(actual_counts[['Type', 'Quarter', 'Simple Assault']]).mark_line().transform_fold(fold=df['Type'].unique().tolist(), as_=['variable', 'value']).encode(
        x='Quarter',
        y='Simple Assault',
        color='Type'
    )   
    st.altair_chart(assault_line, use_container_width=True)
with tab3:
    cartheft_line = alt.Chart(actual_counts[['Type', 'Quarter', 'Theft From Motor Vehicle']]).mark_line().transform_fold(fold=df['Type'].unique().tolist(), as_=['variable', 'value']).encode(
        x='Quarter',
        y='Theft From Motor Vehicle',
        color='Type'
    )  
    st.altair_chart(cartheft_line, use_container_width=True)

