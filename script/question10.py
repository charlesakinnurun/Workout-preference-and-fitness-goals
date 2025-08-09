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