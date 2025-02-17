import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="border_data",
    user="kaushikbasavaraju",
    password="Sunny@123",
    host="localhost",
    port="5432"
)

# Query data
query = "SELECT port_name, SUM(value) AS total_crossings FROM border_crossings GROUP BY port_name ORDER BY total_crossings DESC LIMIT 10;"
df = pd.read_sql(query, conn)

print(df)  # Display data for reference

# Close the connection
conn.close()

# Plot the data using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='total_crossings', y='port_name', data=df)
plt.title('Top 10 Ports by Border Crossings')
plt.xlabel('Total Crossings')
plt.ylabel('Port Name')
plt.show()
