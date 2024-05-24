
# Import necessary libraries
import pandas_datareader.data as web
import datetime

# Set start and end dates
start_date = datetime.datetime(1980, 1, 1)
end_date = datetime.datetime(2024, 1, 1)

# Download data from FRED
gdp = web.DataReader("GDPC1", "fred", start_date, end_date)  # Real GDP data
inflation = web.DataReader("CPIAUCNS", "fred", start_date, end_date)  # Consumer Price Index data (CPI)
unemployment = web.DataReader("UNRATE", "fred", start_date, end_date)  # Unemployment rate data


# Resample to quarterly frequency
gdp_quarterly = gdp.resample('Q').mean()
inflation_quarterly = inflation.resample('Q').mean()
unemployment_quarterly = unemployment.resample('Q').mean()

######
# Import necessary libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Descriptive statistics for real GDP
gdp_summary = gdp.describe()

# Descriptive statistics for inflation
inflation_summary = inflation.describe()

# Descriptive statistics for unemployment
unemployment_summary = unemployment.describe()

# Print summaries
print("Descriptive statistics for real GDP:")
print(gdp_summary)
print("\nDescriptive statistics for inflation:")
print(inflation_summary)
print("\nDescriptive statistics for unemployment:")
print(unemployment_summary)

# Calculate correlation coefficients
correlation = pd.concat([gdp, inflation, unemployment], axis=1).corr()

# Print correlation matrix
print("\nCorrelation coefficients:")
print(correlation)


# Merge dataframes on their indices
merged_data = pd.concat([gdp, inflation, unemployment], axis=1)

# Run multiple linear regression model
X = sm.add_constant(merged_data[['CPIAUCNS', 'UNRATE']])
y = merged_data['GDPC1']
model = sm.OLS(y, X).fit()

# Summary of regression model
print("\nRegression model summary:")
print(model.summary())

################

import pandas_datareader.data as web
import datetime

# Define start and end dates
start_date = datetime.datetime(1980, 1, 1)
end_date = datetime.datetime(2024, 1, 1)

# Download GDP data
gdp = web.DataReader("GDPC1", "fred", start_date, end_date)  # Real GDP data

# Download inflation data (Consumer Price Index)
inflation = web.DataReader("CPIAUCNS", "fred", start_date, end_date)  # Consumer Price Index data (CPI)

# Download unemployment rate data
unemployment = web.DataReader("UNRATE", "fred", start_date, end_date)  # Unemployment rate data

# Save data to Excel
gdp.to_excel("gdp_data.xlsx")
inflation.to_excel("inflation_data.xlsx")
unemployment.to_excel("unemployment_data.xlsx")

#####

import shutil
import os

# Define the paths of the Excel files and the destination directory
excel_files = ["gdp_data.xlsx", "inflation_data.xlsx", "unemployment_data.xlsx"]
destination_directory = os.path.join(os.path.expanduser("~"), "Desktop")

# Copy each Excel file to the destination directory
for file in excel_files:
    source_path = file
    destination_path = os.path.join(destination_directory, file)
    shutil.copy(source_path, destination_path)

print("Excel files copied to desktop successfully!")
