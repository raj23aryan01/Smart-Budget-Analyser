import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
from pypdf import PdfReader


st.set_page_config(
    page_title="Expense Analyzer",
    layout="wide"
)

st.title("Smart Expense & Budget Analyzer")

# PDF EXTRACTION

def extract_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

# PDF TRANSACTION PARSER

def parse_pdf(text):

    rows = []

    lines = text.split("\n")

    for line in lines:

        # Looks for:
        # Description  Category  Amount

        match = re.search(
            r"(.+?)\s+([A-Za-z]+)\s+₹?\s?([\d,]+(?:\.\d+)?)$",
            line.strip()
        )

        if match:

            description = match.group(1)
            category = match.group(2)

            amount = match.group(3).replace(
                ",",
                ""
            )

            rows.append({
                "Description": description,
                "Category": category,
                "Amount": float(amount)
            })

    return pd.DataFrame(rows)


# FILE UPLOAD

uploaded_file = st.file_uploader(
    "Upload CSV or PDF",
    type=["csv", "pdf"]
)


if uploaded_file:

    try:

        if uploaded_file.name.lower().endswith(
            ".csv"
        ):

            df = pd.read_csv(
                uploaded_file
            )

        else:

            text = extract_pdf(
                uploaded_file
            )

            df = parse_pdf(
                text
            )


        if df.empty:

            st.error(
                "No transactions could be detected."
            )

            st.info(
                "For PDFs, the statement must contain "
                "machine-readable text in a recognizable format."
            )

            st.stop()

        # CLEAN DATA

        if "Amount" not in df.columns:

            st.error(
                "The file must contain an Amount column."
            )

            st.stop()


        df["Amount"] = pd.to_numeric(
            df["Amount"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["Amount"]
        )

        # SUMMARY


        total = df["Amount"].sum()

        average = df["Amount"].mean()

        highest = df["Amount"].max()


        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Total Spending",
            f"₹{total:,.2f}"
        )

        col2.metric(
            "Average Transaction",
            f"₹{average:,.2f}"
        )

        col3.metric(
            "Largest Transaction",
            f"₹{highest:,.2f}"
        )

        # DATA

        st.subheader(
            "Transaction Data"
        )

        st.dataframe(
            df,
            use_container_width=True
        )


        # CATEGORY ANALYSIS


        if "Category" in df.columns:

            st.subheader(
                "Spending by Category"
            )

            category_data = (
                df.groupby("Category")
                ["Amount"]
                .sum()
                .sort_values(
                    ascending=False
                )
            )

            st.bar_chart(
                category_data
            )

        # LARGEST TRANSACTIONS


        st.subheader(
            "Top Transactions"
        )

        st.dataframe(
            df.sort_values(
                "Amount",
                ascending=False
            ).head(10),
            use_container_width=True
        )


    except Exception as error:

        st.error(
            f"Could not process file: {error}"
        )


else:

    st.info(
        "Upload a CSV or PDF statement."
    )