# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import yfinance as yf
import  datetime

def show_stock():
    symbol = st.selectbox("Select the stock",("AAPL","GOOG","TSLA","MSFT"))


    ticker_data = yf.Ticker(symbol)
    col1, col2 = st.columns(2)
    with col1:
        start_dt = st.date_input("provide Start date", datetime.date(2019, 7, 6))

    with col2:
        end_dt = st.date_input("provide End date", datetime.date(2022, 7, 6))


    ticker_df = ticker_data.history(period="id",start=start_dt, end = end_dt)
    st.dataframe(ticker_df)
    st.write(f" # {symbol} Stock Chart ")
    st.line_chart(ticker_df["Close"])
    st.write(f" # {symbol} Volume Chart ")
    st.line_chart(ticker_df["Volume"])

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    st.write(" "
             "# Hello Streamlit from python")
    st.write(" # Apple Stock Data ")
    show_stock()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
