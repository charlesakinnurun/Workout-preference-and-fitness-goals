import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Program with highest number of total exercises
max_exercises_idx = df["total_exercises"].idxmax()
max_exercises_program = df.loc[max_exercises_idx,["title","total_exercises"]]

# Display the result
print("The Program with the highest number of exercises is:")
print(max_exercises_program)