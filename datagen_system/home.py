import streamlit as st

st.title("Fictional Data Generator")
st.text(
    "Welcome to the Fictional Data Generator! This tool allows you to generate fictional data for your fintech projects. You can generate data for various categories such as names, addresses, and phone numbers. You can also generate data for custom categories. To get started, select a category from the sidebar.",
    help="This is a tool for generating fictional data for your fintech projects.",
)
st.selectbox("Select a category", ["Income", "Expenses", "Cashflow", "Credit Score"])
st.slider("Select a quantity", 10, 1000, 10)
st.snow()
st.button(
    "Generate Data :sunglasses:",
    help="Click this button to generate fictional data.",
    type="primary",
)
