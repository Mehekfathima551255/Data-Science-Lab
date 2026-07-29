import pandas as pd

# Load Dataset
df = pd.read_csv("employees.csv")

# Clean the Dataset
df = df.dropna()
df = df.drop_duplicates()

# Save the Cleaned Dataset
df.to_csv("cleaned_employees.csv", index=False)

print("Cleaned dataset exported successfully!")
print("\nSaved as: cleaned_employees.csv")

print("\nPreview of Cleaned Dataset:")
print(df)