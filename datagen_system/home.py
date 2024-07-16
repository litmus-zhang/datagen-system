import streamlit as st
from services.data import DataGenerator


data = DataGenerator()

st.title("Fictional Data Generator")
st.text(
    "Welcome to the Fictional Data Generator! This tool allows you to generate fictional data for your fintech projects. You can generate data for various categories such as names, addresses, and phone numbers. You can also generate data for custom categories. To get started, select a category from the sidebar.",
    help="This is a tool for generating fictional data for your fintech projects.",
)
selection = st.selectbox(
    "Select a category",
    ["Income", "Expenses", "Cashflow", "Credit Score", "User Profile"],
)
qty = st.slider("Select a quantity", 10, 1000, 10)
# st.snow()


def generate_data(selection=selection, quantity=qty):
    # Data generation based on
    match selection:
        case "Income":
            res = [data.generate_transaction("card") for _ in range(quantity)]
            st.write(res)

        case "Expenses":
            res = [data.generate_transaction("crypto") for _ in range(quantity)]
            st.write(res)

        case "Cashflow":
            res = [data.generate_datetime() for _ in range(quantity)]
            st.write(res)

        case "Credit Score":
            res = [data.generate_transaction("card") for _ in range(quantity)]
            st.write(res)

        case "User Profile":
            res = [data.generate_person() for _ in range(quantity)]
            st.write(res)
    st.success("Data generation complete!")


st.button(
    "Generate Data :sunglasses:",
    help="Click this button to generate fictional data.",
    type="primary",
    on_click=generate_data(selection, qty),
)
