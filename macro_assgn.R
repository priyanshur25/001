# Load necessary libraries
library(quantmod)

# Set start and end dates
start_date <- as.Date("1980-01-01")
end_date <- as.Date("2024-01-01")

# Download data from FRED
gdp <- getSymbols("GDPC1", src = "FRED", from = start_date, to = end_date, auto.assign = FALSE)  # Real GDP data
inflation <- getSymbols("CPIAUCNS", src = "FRED", from = start_date, to = end_date, auto.assign = FALSE)  # Consumer Price Index data (CPI)
unemployment <- getSymbols("UNRATE", src = "FRED", from = start_date, to = end_date, auto.assign = FALSE)  # Unemployment rate data

# Resample to quarterly frequency
gdp_quarterly <- to.quarterly(gdp, indexAt = "endof", OHLC = FALSE)
inflation_quarterly <- to.quarterly(inflation, indexAt = "endof", OHLC = FALSE)
unemployment_quarterly <- to.quarterly(unemployment, indexAt = "endof", OHLC = FALSE)

# Descriptive statistics for real GDP
gdp_summary <- summary(gdp)

# Descriptive statistics for inflation
inflation_summary <- summary(inflation)

# Descriptive statistics for unemployment
unemployment_summary <- summary(unemployment)

# Print summaries
cat("Descriptive statistics for real GDP:\n")
print(gdp_summary)
cat("\nDescriptive statistics for inflation:\n")
print(inflation_summary)
cat("\nDescriptive statistics for unemployment:\n")
print(unemployment_summary)

# Merge dataframes on their indices
merged_data <- merge.xts(gdp, inflation, unemployment)

# Run multiple linear regression model
model <- lm(GDPC1 ~ CPIAUCNS + UNRATE, data = merged_data)

# Summary of regression model
cat("\nRegression model summary:\n")
print(summary(model))
