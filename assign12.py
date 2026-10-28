import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def to_numeric_marks(value):
    """Convert values like '85,90,78' into their average numeric score."""
    if pd.isna(value):
        return np.nan
    if isinstance(value, str):
        cleaned = value.replace(" ", "")
        parts = cleaned.split(",")
        if len(parts) > 1:
            return float(np.mean([float(part) for part in parts if part]))
        return float(cleaned)
    return float(value)


# Read CSV file
df = pd.read_csv("students.csv")

# Convert Marks column to numeric values
if "Marks" in df.columns:
    df["Marks"] = df["Marks"].apply(to_numeric_marks)

# Display dataset
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Shape of dataset
print("\nShape:")
print(df.shape)

# Column Names
print("\nColumns:")
print(df.columns)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values in numeric columns
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Correlation Matrix
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# Histogram for Marks
if "Marks" in df.columns:
    plt.figure(figsize=(6, 4))
    plt.hist(df["Marks"], bins=5, color="skyblue", edgecolor="black")
    plt.title("Distribution of Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    if matplotlib.get_backend().lower() != "agg":
        plt.show()
    plt.close()

# Box Plot for Marks
if "Marks" in df.columns:
    plt.figure(figsize=(5, 4))
    plt.boxplot(df["Marks"])
    plt.title("Box Plot of Marks")
    plt.ylabel("Marks")
    if matplotlib.get_backend().lower() != "agg":
        plt.show()
    plt.close()

# Scatter Plot: Study Hours vs Marks
if "Study_Hours" in df.columns and "Marks" in df.columns:
    plt.figure(figsize=(6, 4))
    plt.scatter(df["Study_Hours"], df["Marks"], color="red")
    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    if matplotlib.get_backend().lower() != "agg":
        plt.show()
    plt.close()

# Bar Chart for Student Marks
if "Student" in df.columns and "Marks" in df.columns:
    plt.figure(figsize=(8, 4))
    plt.bar(df["Student"], df["Marks"], color="green")
    plt.title("Marks of Students")
    plt.xlabel("Student")
    plt.ylabel("Marks")
    if matplotlib.get_backend().lower() != "agg":
        plt.show()
    plt.close()

print("\nEDA Completed Successfully!")