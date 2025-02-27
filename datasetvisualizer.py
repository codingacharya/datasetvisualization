import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file):
    ext = file.name.split(".")[-1]
    if ext == "csv":
        return pd.read_csv(file)
    elif ext in ["xls", "xlsx"]:
        return pd.read_excel(file)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return None

def plot_charts(df):
    num_cols = df.select_dtypes(include=['number']).columns
    if len(num_cols) < 2:
        st.error("Dataset must have at least two numerical columns for visualization.")
        return
    
    st.subheader("Data Visualizations")
    
    # Scatter Plot
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=num_cols[0], y=num_cols[1], ax=ax)
    st.pyplot(fig)
    
    # Histogram
    fig, ax = plt.subplots()
    sns.histplot(df[num_cols[0]], kde=True, ax=ax)
    st.pyplot(fig)
    
    # Box Plot
    fig, ax = plt.subplots()
    sns.boxplot(data=df[num_cols], ax=ax)
    st.pyplot(fig)
    
    # Pair Plot
    st.pyplot(sns.pairplot(df[num_cols]))
    
    # Correlation Heatmap
    fig, ax = plt.subplots()
    sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    
    # Line Plot
    fig, ax = plt.subplots()
    df[num_cols].plot(kind='line', ax=ax)
    st.pyplot(fig)
    
    # Bar Plot
    fig, ax = plt.subplots()
    df[num_cols].mean().plot(kind='bar', ax=ax)
    st.pyplot(fig)
    
    # Violin Plot
    fig, ax = plt.subplots()
    sns.violinplot(data=df[num_cols], ax=ax)
    st.pyplot(fig)
    
    # KDE Plot
    fig, ax = plt.subplots()
    sns.kdeplot(df[num_cols[0]], shade=True, ax=ax)
    st.pyplot(fig)
    
    # Pie Chart (if applicable)
    if df[num_cols[0]].nunique() < 10:
        fig, ax = plt.subplots()
        df[num_cols[0]].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)

st.title("Dataset Visualizer with 10 Charts")
file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xls", "xlsx"])
if file:
    df = load_data(file)
    if df is not None:
        st.write("## Data Preview")
        st.write(df.head())
        plot_charts(df)
