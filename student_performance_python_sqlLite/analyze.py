import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("students.db")

df = pd.read_sql_query("SELECT * FROM performance", conn)
print("\n=== Student Data ===")
print(df)

avg_scores = pd.read_sql_query("""
SELECT 
    AVG(maths) AS avg_maths,
    AVG(science) AS avg_science,
    AVG(english) AS avg_english
FROM performance
""", conn)

print("\n=== Average Scores ===")
print(avg_scores)

topper = pd.read_sql_query("""
SELECT name, (maths + science + english) AS total
FROM performance
ORDER BY total DESC
LIMIT 1
""", conn)

print("\n=== Top Performer ===")
print(topper)

weak_subject = avg_scores.idxmin(axis=1)[0]
print("\n=== Weakest Subject ===")
print(weak_subject)

avg_scores.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

conn.close()
