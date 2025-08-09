import pandas as pd
import numpy as np
import ast

# Load the DataFrame
df = pd.read_csv("datasets/fitness_workout.csv")

# Step 1: Drop empty rows where most values are NaN.
# I'll fill empty strings with NaN to make sure they are included in the dropna check
df.replace(r'^\s*$',np.nan,regex=True,inplace=True)
df.dropna(how="all",inplace=True)

# Step 2: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 3: Convert "created" and "last_edit" to datetime objects
df["created"] = pd.to_datetime(df["created"])
df["last_edit"] = pd.to_datetime(df["last_edit"])

# Step 4: Convert string representaions of list to actual lists in "level" and "goal" columns
# We'll need to handle any NaN values first to avoid errors
df["level"] = df["level"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
df["goal"] = df["goal"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

# Save the cleaned data to a new CSV file
df.to_csv("datasets/fitness_workout_cleaned.csv")
print("Saved Sucessfully")