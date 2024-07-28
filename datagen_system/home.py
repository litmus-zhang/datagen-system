import streamlit as st
from services.data import DataGenerator
import datetime
import pandas as pd

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
qty = st.slider("Select a quantity", 0, 10000, 10)
# st.snow()


def generate_data(selection=selection, quantity=qty):
    # Data generation based on user selection
    res = []
    match selection:
        case "Income":
            res = [data.generate_transaction("card") for _ in range(quantity)]
            if res:
                st.write(res)
                st.success("Data generation complete!")

        case "Expenses":
            res = [data.generate_transaction("crypto") for _ in range(quantity)]
            if res:
                st.write(res)
                st.success("Data generation complete!")

        case "Cashflow":
            res = [data.generate_cashflow() for _ in range(quantity)]
            if res:
                st.write(res)
                st.success("Data generation complete!")

        case "Credit Score":
            res = [data.generate_credit_score() for _ in range(quantity)]
            if res:
                st.write(res)
                st.success("Data generation complete!")

        case "User Profile":
            res = [data.generate_person() for _ in range(quantity)]
            if res:
                st.write(res)
                st.success("Data generation complete!")
    return res


def action():
    # Generate the data
    result = generate_data(selection, qty)

    # Convert the data to a DataFrame
    df = pd.DataFrame(result)

    # Convert the DataFrame to CSV
    csv = df.to_csv(index=False)

    # Get the current timestamp and format it
    current_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Create columns for buttons
    col1, col2 = st.columns(2)

    # Generate Data button
    col1.button(
        "Generate Data :sunglasses:",
        help="Click this button to generate fictional data.",
        type="primary",
        on_click=generate_data(selection, qty),
    )

    # Download as CSV button
    col2.download_button(
        label="Download as CSV :arrow_down:",
        data=csv,
        file_name=f"{selection}-{qty}-{current_timestamp}.csv",
        mime="text/csv",
        help="Click this button to download the generated data as a CSV file.",
    )


if __name__ == "__main__":
    action()
