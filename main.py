# Student-Marks-Analyzer-
Read marks from CSV then calculate average, max,min per subject and compare students using bar charts.
import pandas as pd 
import matplotlib.pyplot as plt

# Read marks from CSV
df = pd.read_csv('marks.csv')

# Calculate average, max, min 
subject_stats = df.drop(columns=['student']).agg(['mean', 'max', 'min'])

print("Subject Statistics")
print(subject_stats)

df['Total'] = df.drop(columns=['student']).sum(axis=1)

plt.figure(figsize=(10, 6))
plt.bar(df['student'], df['Total'], color='blue', edgecolor='purple')

plt.xlabel('Students', fontsize=20)
plt.ylabel('Total Marks', fontsize=20)
plt.title('Student Performance Comparison', fontsize=20)
plt.grid(axis='y', linestyle='--', alpha=1)

plt.show()


import pandas as pd 
df=pd.read_csv(r"C:\Users\prash\OneDrive\Desktop\marks.csv")
print(df)



