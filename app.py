import streamlit as st
import pandas as pd
from analysis import add_features, topper, top_city

st.title("🎓 Student Performance Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # 🔹 Add features
    df = add_features(df)

    # 🔹 Full Data
    st.subheader("📊 Full Data")
    st.dataframe(df)

    # 🔹 Top 3 Students
    st.subheader("🏆 Top 3 Students")
    st.dataframe(topper(df))

    # 🔹 Best City
    st.subheader("🌆 Best City")
    st.dataframe(top_city(df))

    # 🔹 Filter Section (INSIDE IF 🔥)
    st.subheader("🔍 Filter Data")

    city = st.selectbox("Select City", df["city"].unique())
    grade = st.selectbox("Select Grade", df["grade"].unique())

    filtered_df = df[(df["city"] == city) & (df["grade"] == grade)]

    st.dataframe(filtered_df)