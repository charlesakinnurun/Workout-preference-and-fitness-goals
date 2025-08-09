
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Programs that require "Full Gym" equipment and are for the "Advanced" level
full_gym_advanced_programs = df[
    (df["equipment"] == "Full Gym") &
    (df["level"].apply(lambda x:"Advanced" in x if isinstance(x,list) else False))
]

# Display the result 
print("Programs that require 'Full Gym' eqipment and are for 'advanced' level users")
print(full_gym_advanced_programs["title"])