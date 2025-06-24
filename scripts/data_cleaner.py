import pandas as pd
import os
from datetime import datetime
import csv

# Load data
file_path = "raw_data/sales_data.csv"
df = pd.read_csv(file_path, encoding='latin1')

print(df.head())

# Drop missing values
# Remove blanks and duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Strip spaces inside string values
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Convert date columns
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Add 'total' column if missing
if 'total' not in df.columns and {'price', 'quantity'}.issubset(df.columns):
    df['total'] = df['price'] * df['quantity']

print(df.columns.tolist())

# Create summary
summary = {
    "Total Orders": len(df),
    "Total Sales": df['sales'].sum(),
    "Total Profit": df['profit'].sum(),
    "Top 5 Cities": df['city'].value_counts().head(5).to_dict(),
    "Top 5 Products": df['product_name'].value_counts().head(5).to_dict(),
    "Sales by Region": df.groupby('region')['sales'].sum().to_dict()
}


# Get the full path to the logs folder
base_path = os.path.dirname(os.path.dirname(__file__))  # Goes up to data_pipeline_project
log_folder = os.path.join(base_path, "logs")

# Generate a dynamic filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
log_file = os.path.join(log_folder, f"summary_{timestamp}.txt")

# Write to file
with open(log_file, 'w') as f:
    f.write(" Log created successfully")

    for key, value in summary.items():
        f.write(f"{key}: {value}\n")

# Save cleaned data
# Base directory (data_pipeline_project)
base_path = os.path.dirname(os.path.dirname(__file__))

# Cleaned data folder
cleaned_folder = os.path.join(base_path, "cleaned_data")
os.makedirs(cleaned_folder, exist_ok=True)  # Creates if not exists

# Save path with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_file = os.path.join(cleaned_folder, f"cleaned_sales_{timestamp}.csv")

# Save cleaned data
df.to_csv(output_file, index=False, encoding='utf-8')

print(" Cleaned data saved at:", output_file)

print(" Data cleaned and summary generated!")

# Set path to summary.csv (in your main project folder)
summary_file = os.path.join(base_path, "summary.csv")

# Save summary to CSV
with open(summary_file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Metric", "Value"])  # Add headers
    for key, value in summary.items():
        writer.writerow([key, value])

