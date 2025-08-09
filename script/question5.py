import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Convert the date column to datetime object
df["created"] = pd.to_datetime(df["created"])

# Total number of workouts created in each year
workouts_per_year = df["created"].dt.year.value_counts().sort_index()
print("Total number of workouts created per year")
print(workouts_per_year)