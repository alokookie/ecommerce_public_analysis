import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analisis E-Commerce")

# load data dari csv
top_3 = pd.read_csv('top_3.csv')
bottom_3 = pd.read_csv('bottom_3.csv')

avg_items = pd.read_csv('avg_items.csv')['avg_items'].iloc[0]

avg_monthly = pd.read_csv('avg_monthly.csv')

# clean data
avg_monthly['month'] = avg_monthly['month'].astype(str)
avg_monthly['price'] = pd.to_numeric(avg_monthly['price'], errors='coerce')
avg_monthly = avg_monthly.dropna(subset=['price'])

# Kategori produk yang sering dan paling jarang dibeli customer
st.subheader("Kategori Produk")

col1, col2 = st.columns(2)

with col1:
    st.write("Top 3 Kategori Paling Sering Dibeli")
    st.dataframe(top_3)

with col2:
    st.write("Top 3 Kategori Paling Jarang Dibeli")
    st.dataframe(bottom_3)

#Rata-rata jumlah produk dalam satu pesanan
st.subheader("Rata-rata Produk per Order")
st.metric("Rata-rata", f"{avg_items:.2f}")

# tren tranksaksi bulanan 
st.subheader("Tren Transaksi Bulanan")

avg_monthly = avg_monthly.sort_values('month')

fig, ax = plt.subplots(figsize=(8, 3))

ax.plot(
    avg_monthly['month'].values,
    avg_monthly['price'].values
)

ax.set_xlabel("Month")
ax.set_ylabel("Price")
ax.tick_params(axis='x', rotation=45)

st.pyplot(fig, clear_figure=True)