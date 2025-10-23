import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import glob
import os

st.set_page_config(page_title="Electronic Gadget Sales Dashboard", layout="wide")
st.title("Electronic Gadget Sales Analysis")
st.markdown("By Obumneme Nkeanyadi")

# Load all CSV files
data_files = glob.glob(os.path.join(os.getcwd(), "Sales_*.csv"))
dt = [pd.read_csv(f) for f in data_files]
df = pd.concat(dt)



# Data Cleaning
df.dropna(how='all', inplace=True)
df = df[df['Quantity Ordered'].str.isdigit()]
df = df[df['Price Each'].str.isdigit()]
df = df[df['Order ID'].str.isdigit()]
df['Quantity Ordered'] = df['Quantity Ordered'].astype(int)
df['Price Each'] = df['Price Each'].astype(float)
df['Order ID'] = df['Order ID'].astype(int)
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df.drop_duplicates(inplace=True)
df['Month'] = df['Order Date'].dt.month_name()
df['Day'] = df['Order Date'].dt.day_name()
df['Time'] = df['Order Date'].dt.time
df['Amount'] = (df['Quantity Ordered'] * df['Price Each']).round(2)

df['City'] = df['Purchase Address'].apply(lambda City: City.split(',')[-2])

# Sidebar Filters

st.sidebar.header('Filters')
# Add checks for columns existence
city_col = 'City' if 'City' in df.columns else None
sales_person_col = 'Sales Person' if 'Sales Person' in df.columns else None

if city_col:
    city = st.sidebar.multiselect('Select City', options=df[city_col].unique(), default=df[city_col].unique())
else:
    city = None
if sales_person_col:
    sales_reps = st.sidebar.multiselect('Select Sales Person', options=df[sales_person_col].unique(), default=df[sales_person_col].unique())
else:
    sales_reps = None
products = st.sidebar.multiselect('Select Product', options=df['Product'].unique(), default=df['Product'].unique())

# Filter DataFrame
df_filtered = df.copy()
if city_col and city is not None:
    df_filtered = df_filtered[df_filtered[city_col].isin(city)]
if sales_person_col and sales_reps is not None:
    df_filtered = df_filtered[df_filtered[sales_person_col].isin(sales_reps)]
df_filtered = df_filtered[df_filtered['Product'].isin(products)]

# KPIs
Total_Products = df_filtered['Product'].nunique()
No_of_City = df_filtered['City'].nunique()
Quantity_Ordered = df_filtered['Quantity Ordered'].sum()
Revenue = df_filtered['Amount'].sum()

# KPI Cards
st.subheader("Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Products", Total_Products)
kpi2.metric("No. of Cities", No_of_City)
kpi3.metric("Quantity Ordered", Quantity_Ordered)
kpi4.metric("Revenue", f"${Revenue:,.2f}")

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
mon = df_filtered.groupby('Month')['Amount'].sum().reset_index()
fig_mon = px.bar(mon, x='Month', y='Amount', title='Monthly Sales Trend For 2019', color='Amount', color_continuous_scale='Blues')
st.plotly_chart(fig_mon, use_container_width=True)

# Weekly Sales Trend
st.subheader("Weekly Sales Trend")
weekly = df_filtered.groupby('Day')['Amount'].sum().reset_index()
fig_week = px.line(weekly, x='Day', y='Amount', title='Weekly Sales Trend For 2019', markers=True)
st.plotly_chart(fig_week, use_container_width=True)

# Product Sales Performance
st.subheader("Product Sales Performance")
per = df_filtered.groupby('Product')[['Amount', 'Quantity Ordered']].sum().sort_values(by='Quantity Ordered', ascending=False).reset_index()
fig_prod = px.bar(per, x='Product', y=['Amount', 'Quantity Ordered'], barmode='group', title='Product Sales Performance')
st.plotly_chart(fig_prod, use_container_width=True)

# City with Highest Revenue
st.subheader("City with The Highest Revenue")
city = df_filtered.groupby(['City', 'Product'])['Amount'].sum().reset_index()
fig_city = px.bar(city, x='City', y='Amount', color='Product', title='Sales By City', barmode='group')
st.plotly_chart(fig_city, use_container_width=True)

# Show Data
with st.expander("Show Raw Data"):
    st.dataframe(df_filtered)
