# Time-series-crime-prediction
[![image](https://github.com/dmayall/Human-Trafficking-Analysis/assets/108638892/140d4fca-4a91-4930-ae95-2860b7a611fd)](https://time-series-crime-prediction.streamlit.app/)
## Introduction
This project has a goal to be able to predict the amount of crime to occur in each quarter for each census tract of future years. using two models (LSTM and ARIMA) I aimed to take two different approaches to see what would work best. The LSTM approach took in other arguments aside from the sequence itself which included:

- Gas Price (per census tract)
- Weather including tempature and rainfall (per census tract)
- Percent enrolled in k-12 (per census tract for each year)
- Median income (per census tract for each year) 

Predicting the amount of crime in the future for each census tract could better help police prepare based on those predictions. 

## Data Source
This data is found in the following website:
- https://data.charlottenc.gov/datasets/charlotte::cmpd-incidents-1/about'
- https://data.census.gov/
- All other data sources are provided in the code

## Model/NN Used
These are articles on the Arima modle and LSTM NN below:
- Arima: https://people.duke.edu/~rnau/411arim.htm
- LSTM: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

## Data Preparation 
- Grouped all years together
- Combined the different data sets
- Filtered to desired crimes (Theft from motor vehicle, simple assualt, adn all other thefts)
- Gathered census tract data through ArcGis and then imported that data into python
- seperated teh data into a dictionary with each census tract as a key
- Put the data for each key into a sequential from that could be read by the algorithm and lstm
