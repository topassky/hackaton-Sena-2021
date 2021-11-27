import yfinance as yf
import streamlit as st
from GUI_pandas import Gui_pandas

data_pandas = Gui_pandas("dataset.csv")

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
marco_datos = data_pandas.dataFrame_grafica()

#print(marco_datos.iloc[:,[3]])

st.line_chart(marco_datos.iloc[:,[3]])
    