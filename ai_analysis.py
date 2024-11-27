import pandas as pd
import mysql.connector
from sklearn.cluster import KMeans

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="CriminalRecordsDB"
)
cursor = conn.cursor()

# Fetch data from the database
query = "SELECT criminal_id, name, age, crime_id, arrest_date FROM Criminals"
cursor.execute(query)
data = cursor.fetchall()

# Load data into a pandas DataFrame
columns = ["criminal_id", "name", "age", "crime_id", "arrest_date"]
df = pd.DataFrame(data, columns=columns)

# Perform AI-based analysis (example: clustering by age and crime type)
# Simulated feature extraction
df["crime_type"] = df["crime_id"] % 3  # Example crime types: 0, 1, 2
features = df[["age", "crime_type"]]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(features)

# Save analysis results into the AI_Analysis table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO AI_Analysis (criminal_id, pattern, confidence)
        VALUES (%s, %s, %s)
    """, (row["criminal_id"], f"Cluster {row['cluster']}", 0.95))

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("AI analysis completed and saved to the database.")