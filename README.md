# 🌱 Crop Insight: Interactive Dark-Mode Dashboard

A high-performance data visualization tool built with **Python**, **Streamlit**, and **Plotly** to analyze soil nutrients and environmental factors for optimal crop recommendation.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=Plotly&logoColor=white)

## 🌌 Overview
This project provides an interactive, dark-themed interface to explore the **Crop Recommendation Dataset**. It helps users understand the correlation between Nitrogen (N), Phosphorus (P), Potassium (K), and environmental variables like Temperature, Rainfall, and pH levels.

### **Key Features**
* **Dynamic Filtering:** Compare specific crops side-by-side using the sidebar.
* **Nutrient Profiling:** Bar and Box plots to visualize N-P-K requirements.
* **Climate Analysis:** Scatter plots showing the relationship between Rainfall and Temperature.
* **Correlation Heatmap:** Statistical analysis of how soil factors influence one another.
* **Dark UI:** Optimized for high-contrast visibility and modern aesthetics.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/crop-insight-dark-dashboard.git](https://github.com/your-username/crop-insight-dark-dashboard.git)
cd crop-insight-dark-dashboard
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('Crop_Recommendation.csv')

# Set dark background style for matplotlib
plt.style.use('dark_background')

# Plot 1: Average Nutrient Requirements per Crop (Black Background)
avg_nutrients = df.groupby('Crop')[['Nitrogen', 'Phosphorus', 'Potassium']].mean().sort_values(by='Nitrogen')
fig1, ax1 = plt.subplots(figsize=(15, 7))
avg_nutrients.plot(kind='bar', stacked=True, ax=ax1, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
ax1.set_title('Average Nutrient Requirements (N, P, K) per Crop', color='white', fontsize=16)
ax1.set_ylabel('Nutrient Value', color='white')
ax1.set_xlabel('Crop', color='white')
plt.xticks(rotation=45, color='white')
plt.yticks(color='white')
plt.tight_layout()
plt.savefig('nutrient_distribution_dark.png', facecolor='black')

# Plot 2: Temperature vs. Rainfall Scatter Plot (Black Background)
plt.figure(figsize=(12, 7))
sns.scatterplot(data=df, x='Temperature', y='Rainfall', hue='Crop', palette='viridis', alpha=0.7)
plt.title('Temperature vs. Rainfall across different Crops', color='white', fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', ncol=2, facecolor='black', edgecolor='white', labelcolor='white')
plt.tight_layout()
plt.savefig('temp_vs_rainfall_dark.png', facecolor='black')

# Plot 3: Correlation Heatmap (Black Background)
plt.figure(figsize=(10, 8))
corr = df.drop('Crop', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='magma', fmt=".2f", annot_kws={"color": "white"})
plt.title('Correlation Heatmap of Soil and Environmental Factors', color='white', fontsize=16)
plt.tight_layout()
plt.savefig('correlation_heatmap_dark.png', facecolor='black')

print("Dark themed charts generated successfully.")

