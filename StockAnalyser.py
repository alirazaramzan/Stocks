import streamlit as st
import yfinance as yf

# Set the title of the app
st.title('Stock Market Analyzer')

# Get user input for the stock symbol
stock_symbol = st.text_input('Enter a stock symbol (e.g., MSN for Microsoft')

# Get historical stock data
stock_data = yf.Ticker(stock_symbol).history(period='max')

# Display the stock data
st.subheader('Stock Data')
st.write(stock_data)

# Calculate the percentage change in stock price
stock_data['Price_Change'] = stock_data['Close'].pct_change() * 100

# Find the maximum price drop and corresponding date
max_drop = stock_data['Price_Change'].min()
max_drop_date = stock_data['Price_Change'].idxmin()

# Display the maximum price drop information
st.subheader('Maximum Price Drop')
st.write('Percentage Change:', round(max_drop, 2), '%')
st.write('Date:', max_drop_date)

# Determine the recommendation
if max_drop < 0:
    st.subheader('Recommendation')
    st.write('*The stock has experienced a maximum price drop. Consider to checkout your stock ASAP!*')