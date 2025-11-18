import sqlite3
import pandas as pd

df = pd.read_csv("data.csv")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS performance (
    student_id INTEGER,
    name TEXT,
    maths INTEGER,
    science INTEGER,
    english INTEGER
)
""")

cursor.execute("DELETE FROM performance")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO performance (student_id, name, maths, science, english)
        VALUES (?, ?, ?, ?, ?)
    """, (
        int(row["student_id"]), row["name"],
        int(row["maths"]), int(row["science"]), int(row["english"])
    ))

conn.commit()
conn.close()

print("Database created and data inserted successfully!")
