import pandas as pd
import numpy as np
import ast
import re
from collections import Counter

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Correct the data types for `level` and `goal` columns
# as they were saved as strings in the CSV
df['created'] = pd.to_datetime(df['created'])
df['last_edit'] = pd.to_datetime(df['last_edit'])
df['level'] = df['level'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
df['goal'] = df['goal'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Average "time_per_workout" for "Beginner" level users
beginner_workouts = df[df["level"].apply(lambda x: "Beginner" in x if isinstance(x,list) else False)]
avg_time = beginner_workouts["time_per_workout"].mean()
print(f"The average time per workout for beginner-level program is {avg_time:.2f} minutes")