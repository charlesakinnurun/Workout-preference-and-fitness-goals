import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Average "total_exercises" for programs with the program_length of 12 weeks
twelve_week_programs = df[df["program_length"] == 12]
avg_exercises_12_weeks = twelve_week_programs["total_exercises"].mean()
print(f"The average number of total exercise of 12-week programs is {avg_exercises_12_weeks}")