import sqlite3
import pandas as pd

'''CONNECT TO SQLITE3'''
conn = sqlite3.connect("profiles.db")
cursor = conn.cursor()

'''IF THE TABLE IS PRESENT DROP'''
cursor.execute("DROP TABLE IF EXISTS profiles")


'''CREATE THE TABLE'''
cursor.execute("""
CREATE TABLE IF NOT EXISTS profiles (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    designation TEXT,
    department TEXT
)
""")

'''READ THE EXCEL FILE'''
df = pd.read_excel("Sample_Input.xlsx")

rows = []
for _, row in df.iterrows():
    try:
        rows.append((
            str(row["ID"]),
            row["Name"],
            row["email"],
            str(row["Phone"]) if pd.notna(row["Phone"]) else None,
            row["Designation"],
            row["Department"]
        ))
    except KeyError as e:
        print(f"Skipping row due to missing column: {e}")
        continue

'''INSERT DATA TO SQLITE'''
cursor.executemany("INSERT OR IGNORE INTO profiles VALUES (?, ?, ?, ?, ?, ?)", rows)
conn.commit()
conn.close()

print(f"Successfully inserted the data into profiles.db")