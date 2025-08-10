## Introduction
The dataset contains fitness workout programs. Each row represents a unique workout program, and the columns provide detailed information about each one. The data is suitable for analysis of workout trends, program characteristics, and user-focused fitness options.
## Data Cleaning
```python
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
```
## Analysis
Here are 10 analytical questions that you can solve using the pandas library:
1. What is the average time_per_workout for programs targeted at Beginner level users?
2. How many unique equipment types are mentioned in the dataset?
3. Which goal is the most popular across all workouts, and how many workouts are associated with it?
4. Can you find the program that has the highest number of total_exercises and its corresponding title?
5. What is the total number of workouts created in each year?
6. Which program has the longest duration between its created date and its last_edit date?
7. What is the distribution of program_length values, and what is the most common length?
8. List all the programs that require Full Gym equipment and are for the Advanced level.
9. What is the average number of total_exercises for programs with a program_length of 12 weeks?
10. Can you identify the top 5 most frequently mentioned words in the description column?
#### What is the average time_per_workout for programs targeted at Beginner level users?
```python
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
```
#### How many unique equipment types are mentioned in the dataset?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Number of unique equipment types
unique_equipment = df["equipment"].nunique()
print(f"There are {unique_equipment} unique equipment types mentioned in the dataset")
```
#### Which goal is the most popular across all workouts, and how many workouts are associated with it?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Most Popular goal
goal_exploded = df.explode("goal")
most_popular_goal = goal_exploded["goal"].value_counts().idxmax()
most_popular_count = goal_exploded["goal"].value_counts().max()

# Display the result
print(f"The most popular goal is '{most_popular_goal}' with {most_popular_count} associated workouts")
```
#### Can you find the program that has the highest number of total_exercises and its corresponding title?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Program with highest number of total exercises
max_exercises_idx = df["total_exercises"].idxmax()
max_exercises_program = df.loc[max_exercises_idx,["title","total_exercises"]]

# Display the result
print("The Program with the highest number of exercises is:")
print(max_exercises_program)
```
#### What is the total number of workouts created in each year?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Convert the date column to datetime object
df["created"] = pd.to_datetime(df["created"])

# Total number of workouts created in each year
workouts_per_year = df["created"].dt.year.value_counts().sort_index()
print("Total number of workouts created per year")
print(workouts_per_year)
```
#### Which program has the longest duration between its created date and its last_edit date?
```python
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
```
#### What is the distribution of program_length values, and what is the most common length?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Distribution of "program_length" values and the most common length
program_length_counts = df["program_length"].value_counts()
most_common_length = program_length_counts.idxmax()
print("Distribution of program lengths (in weeks):")
print(program_length_counts)
print(f"The most common program length is {int(most_common_length)} weeks")
```
#### List all the programs that require Full Gym equipment and are for the Advanced level.
```python
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
```
#### What is the average number of total_exercises for programs with a program_length of 12 weeks?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Average "total_exercises" for programs with the program_length of 12 weeks
twelve_week_programs = df[df["program_length"] == 12]
avg_exercises_12_weeks = twelve_week_programs["total_exercises"].mean()
print(f"The average number of total exercise of 12-week programs is {avg_exercises_12_weeks}")
```
#### Can you identify the top 5 most frequently mentioned words in the description column?
```python
import pandas as pd
import re
from collections import Counter

# Load the cleaned data
df = pd.read_csv("datasets/fitness_workout_cleaned.csv")

# Top 5 most frequently mentioned words in the "description" column
# Drop rows where "description" is NaN before processing
df_with_decriptions = df.dropna(subset=["description"]).copy()
text_data = ' '.join(df_with_decriptions["description"].astype(str).str.lower())
words = re.findall(r'\b\w+\b', text_data)

# Filter out some common words
stopwords = {'the', 'a', 'an', 'and', 'or', 'to', 'for', 'in', 'is', 'it', 'with', 'on', 'day'}
filtered_words = [word for word in words if word not in stopwords and len(word) > 3]

word_counts = Counter(filtered_words)
top_5_words = word_counts.most_common(5)
print("The top 5 most frequently mentioned words in the description column are")
for word,count in top_5_words:
    print(f"- '{word}' (count: {count})")
```
