import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Textile Forecast Dashboard", layout="wide")

st.title("🧵 Textile Demand Forecast Dashboard")
st.markdown("Welcome! This dashboard shows the final outputs from our demand forecasting and item recommendation models for textiles.")

st.subheader("📊 Total Sales per Year")
try:
    img1 = Image.open("cell2_total_sales_year.png")
    st.image(img1, use_container_width=True)
except FileNotFoundError:
    st.error("Image for Total Sales per Year not found.")

st.subheader("📋 Top 4 Most Sold Materials by Period")
try:
    df_items = pd.read_excel("most_sold_materials_by_period.xlsx")
    st.dataframe(df_items)
except FileNotFoundError:
    st.error("Excel file for Most Sold Materials not found.")

st.subheader("📈 Predicted Material Sales (Jan 2025 – Mar 2025)")
try:
    df_cell7 = pd.read_excel("forecast_materials.xlsx")
    st.dataframe(df_cell7)
except FileNotFoundError:
    try:
        img7 = Image.open("cell7_top_materials.png")
        st.image(img7, use_container_width=True)
    except FileNotFoundError:
        st.error("Forecast table or image not found.")

st.subheader("🔮 Forecast Graph: Total Sales (XGBoost)")
try:
    img3 = Image.open("cell11_forecast_xgboost.png")
    st.image(img3, use_container_width=True)
except FileNotFoundError:
    st.error("Forecast graph image not found.")

st.subheader("📋 Top 5 Items for Most Sold Material by Period")
try:
    df_items = pd.read_excel("top5_items_by_period.xlsx")
    st.dataframe(df_items)
except FileNotFoundError:
    st.error("Excel file for Top 5 Items not found.")

st.subheader("📌 Recommended Items for Restock")
try:
    df_items = pd.read_excel("Top9_Unique_Items_Per_Material_Last6Months.xlsx")
    st.dataframe(df_items)
except FileNotFoundError:
    st.error("Excel file for Top 9 Items not found.")

try:
    img4 = Image.open("cell12_predicted_materials.png")
    st.image(img4, use_container_width=True)
except FileNotFoundError:
    st.error("Recommended items chart image not found.")
