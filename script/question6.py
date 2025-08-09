import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")
# Convert the "created" and "last_edit" column to datetime objects
df["created"] = pd.to_datetime(df["created"])
df["last_edit"] = pd.to_datetime(df["last_edit"])

# Program with the longest duration between "created" and "last_edit" dates
df["duration"] = df["last_edit"] - df["created"]
longest_duration_idx = df["duration"].idxmax()
longest_duration_program = df.loc[longest_duration_idx,["title","duration"]]
print("The program with the longest duration between creation and last edit is:")
print(longest_duration_program)