import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Distribution of "program_length" values and the most common length
program_length_counts = df["program_length"].value_counts()
most_common_length = program_length_counts.idxmax()
print("Distribution of program lengths (in weeks):")
print(program_length_counts)
print(f"The most common program length is {int(most_common_length)} weeks")