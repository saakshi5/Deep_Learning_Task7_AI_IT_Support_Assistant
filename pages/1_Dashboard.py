import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration for a wider layout
st.set_page_config(layout="wide")

st.title("📊 Incident Dashboard")

# Load data
df = pd.read_csv("data/incidents.csv")

# Custom CSS for KPI Cards
st.markdown("""
    <style>
    .kpi-card {
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #4A90E2; /* Nice blue border */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 10px;
    }
    .kpi-label {
        font-size: 16px;
        color: #666666; /* Subtle grey for labels */
        font-weight: 500;
        margin-bottom: 5px;
    }
    .kpi-value-1 {
        font-size: 34px;
        color: #E74C3C; /* Bold crimson red for total incidents */
        font-weight: bold;
    }
    .kpi-value-2 {
        font-size: 34px;
        color: #2ECC71; /* Vibrant green for categories count */
        font-weight: bold;
    }
    /* Dark mode overrides (optional, ensures text remains readable) */
    @media (prefers-color-scheme: dark) {
        .kpi-card { background-color: #1E1E1E; border-color: #4A90E2; }
        .kpi-label { color: #BBBBBB; }
    }
    </style>
""", unsafe_allow_html=True) # Fixed parameter here

# KPI Cards Section
kpi1, kpi2 = st.columns(2)

with kpi1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Incidents</div>
            <div class="kpi-value-1">{len(df)}</div>
        </div>
    """, unsafe_allow_html=True) # Fixed parameter here

with kpi2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Categories</div>
            <div class="kpi-value-2">{df["category"].nunique()}</div>
        </div>
    """, unsafe_allow_html=True) # Fixed parameter here

# Add a divider for better visual structure
st.divider()

# Charts Section
col1, col2 = st.columns(2)

with col1:
    fig = px.pie(df, names="category", title="Incident Distribution")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    category_counts = df["category"].value_counts().reset_index()
    category_counts.columns = ["category", "count"]
    
    fig2 = px.bar(
        category_counts, 
        x="category", 
        y="count", 
        title="Incidents by Category"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Data Table Section
st.subheader("Incident Dataset")
st.dataframe(df, use_container_width=True)
