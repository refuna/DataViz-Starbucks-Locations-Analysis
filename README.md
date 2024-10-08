# Starbucks Growth Strategy Dashboard

## Project Overview

This project is an interactive web-based dashboard built using **Streamlit** and **Plotly**. It aims to provide insights into Starbucks' global growth strategy by analyzing store distribution, ownership models, coffee consumption trends, and the nutritional content of Starbucks food and beverages. The dashboard allows users to explore Starbucks' expansion across different regions and how coffee consumption correlates with store density.

## Key Features

### 1. **Global Starbucks Store Distribution**
   - **World Map Visualization**: Displays Starbucks store locations worldwide with hover information about each store.
   - **Country-Level Analysis**: Visualizes the number of stores per country and city.
   - **U.S. State-Level Analysis**: Focuses on the distribution of stores across U.S. states.
   - **Continent-Level Distribution**: Shows store distribution hierarchically by continent and country using a sunburst chart.

### 2. **Coffee Consumption & Store Correlation**
   - **Per Capita Coffee Consumption vs Store Count**: Scatter plot showing the correlation between the number of Starbucks stores and per capita coffee consumption.
   - **Total Coffee Consumption by Country**: A pie chart visualizing coffee consumption share for each country.

### 3. **Ownership Type Analysis**
   - **Ownership Type per Country**: Histogram showing the ownership model (company-owned vs. licensed) for Starbucks stores across various countries.

### 4. **Nutritional Analysis of Food & Drinks**
   - **Food Calorie & Carb. Analysis**: Bar charts that provide insights into calorie and carbohydrate consumption from different Starbucks food items.
   - **Caffeine Content in Beverages**: Visualization of caffeine content in selected Starbucks beverages.
   - **Beverage Size and Calorie Comparison**: A detailed comparison of how different beverage sizes affect calorie content.

## Project Structure

The project consists of several components and data files used to create the dashboard:

```plaintext
📂 Starbucks Growth Strategy Project
│
├── starbucks_growth_strategy.py      # Main Streamlit app code
├── starbucks_drink.csv               # Data for Starbucks drinks
├── starbucks_food.csv                # Data for Starbucks food items
├── directory.csv                     # Starbucks store locations dataset
├── CoffeeConsumption.csv             # Coffee consumption data per country
└── README.md                         # Documentation
