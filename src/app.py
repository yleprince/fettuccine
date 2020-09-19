import pandas as pd
import streamlit as st

st.write(
    """
# Facebook data analyser 👍️
"""
)

PATH = "data/"
df = pd.read_csv(f"{PATH}googletrends_world.csv")
df.index = pd.to_datetime(df.month)
df.drop("month", axis="columns", inplace=True)

st.line_chart(df, width=40)
