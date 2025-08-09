import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Number of unique equipment types
unique_equipment = df["equipment"].nunique()
print(f"There are {unique_equipment} unique equipment types mentioned in the dataset")
