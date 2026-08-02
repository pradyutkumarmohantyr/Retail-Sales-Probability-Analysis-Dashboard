import pandas as pd
import sqlite3

# Load your cleaned CSV
df = pd.read_csv("../data/processed/superstore_clean.csv")
# Create/connect to SQLite database
conn = sqlite3.connect("../database/superstore.db")
# Write dataframe to SQLite
df.to_sql(
    "superstore_clean",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Database created successfully!")
