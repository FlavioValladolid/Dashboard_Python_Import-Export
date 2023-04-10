import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="General Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

df = pd.read_excel(
    io="./Files/Saldos.xlsx",
    engine="openpyxl",
    sheet_name="sheet1",
    #skiprows=3,
    usecols="A:J",
    nrows=1000,

)

st.dataframe(df)