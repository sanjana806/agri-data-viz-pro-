import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Crop Recommendation Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Crop_Recommendation.csv')
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filter Options")
all_crops = sorted(df['Crop'].unique())
selected_crops = st.sidebar.multiselect("Select Crops to Compare", all_crops, default=all_crops[:5])

# Filtered data
filtered_df = df[df['Crop'].isin(selected_crops)]

# Header
st.title("🌱 Crop Recommendation & Soil Analysis Dashboard")
st.markdown("Analyze the relationship between soil nutrients, environmental conditions, and crop types.")

# Key Metrics Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Crops", len(all_crops))
col2.metric("Avg Rainfall", f"{df['Rainfall'].mean():.2f} mm")
col3.metric("Avg Temp", f"{df['Temperature'].mean():.2f} °C")
col4.metric("Avg pH", f"{df['pH_Value'].mean():.2f}")

# Main Visualizations
tab1, tab2, tab3 = st.tabs(["Nutrient Analysis", "Environmental Factors", "Correlations"])

with tab1:
    st.subheader("Distribution of Soil Nutrients (N, P, K)")
    nutrient = st.selectbox("Select Nutrient", ["Nitrogen", "Phosphorus", "Potassium"])
    fig_nut = px.box(filtered_df, x="Crop", y=nutrient, color="Crop", 
                     title=f"{nutrient} Levels across Selected Crops")
    st.plotly_chart(fig_nut, use_container_width=True)

    st.subheader("Average Nutrient Requirements")
    avg_df = filtered_df.groupby('Crop')[['Nitrogen', 'Phosphorus', 'Potassium']].mean().reset_index()
    fig_avg = px.bar(avg_df, x="Crop", y=["Nitrogen", "Phosphorus", "Potassium"], 
                     barmode="group", title="Average N-P-K comparison")
    st.plotly_chart(fig_avg, use_container_width=True)

with tab2:
    st.subheader("Climate vs Rainfall Relationship")
    fig_scatter = px.scatter(filtered_df, x="Temperature", y="Rainfall", color="Crop",
                             size="Humidity", hover_data=['pH_Value'],
                             title="Temperature vs Rainfall (Size = Humidity)")
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    st.subheader("Feature Correlation Heatmap")
    corr = df.drop('Crop', axis=1).corr()
    fig_heat = px.imshow(corr, text_auto=True, aspect="auto", 
                         color_continuous_scale='RdBu_r', title="Correlation Matrix")
    st.plotly_chart(fig_heat, use_container_width=True)

# Data Table
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)