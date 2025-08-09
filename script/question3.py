import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Most Popular goal
goal_exploded = df.explode("goal")
most_popular_goal = goal_exploded["goal"].value_counts().idxmax()
most_popular_count = goal_exploded["goal"].value_counts().max()

# Display the result
print(f"The most popular goal is '{most_popular_goal}' with {most_popular_count} associated workouts")