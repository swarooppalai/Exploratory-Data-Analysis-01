# US Accidents Exploratory Data Analysis (EDA)

This repository contains a Python script for Exploratory Data Analysis (EDA) on US accidents using the data from the file 'US_Accidents_March23.csv'.

## Prerequisites

Make sure you have the required dependencies installed. You can install them using the following:

```bash
pip install pandas seaborn folium
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/US-Accidents-EDA.git
cd US-Accidents-EDA
```

2. Run the script:

```bash
python US_Accidents_EDA.py
```

## Overview

The EDA script covers the following aspects:

1. **Importing Data:**
   - Reads the data from the CSV file ('US_Accidents_March23.csv').

2. **Data Overview:**
   - Prints basic information about the dataset using `df.info()` and `df.describe()`.

3. **Missing Values:**
   - Calculates and plots the percentage of missing values for each column.

4. **City/State Analysis:**
   - Analyzes the number of accidents in different cities and states.
   - Plots the top 10 cities and states with the most accidents.

5. **Start Time Analysis:**
   - Extracts and analyzes the hour, day, and month from the 'Start_Time' column.
   - Plots the distribution of accidents based on day and hour.
   - Examines the data for specific years ('2021' and '2022').

6. **Source of Data:**
   - Visualizes the distribution of data sources.

7. **Geographical Analysis:**
   - Creates scatter and heatmap plots using latitude and longitude data.

8. **Accidents per Capita:**
   - Integrates population data from the 'population_by_zip_2010.csv' file.
   - Analyzes the number of accidents per capita for different states.

## Results

The EDA provides insights into accident patterns, geographical distribution, and temporal variations. The visualizations aid in understanding the data and identifying potential areas for further analysis.

Feel free to explore and modify the script based on your specific requirements.