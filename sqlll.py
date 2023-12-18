
import mysql.connector

# Replace with your database credentials
host = "192.168.18.245"
user = "pythondb_test"
password = "PYt3StDB75S"
database = "pythondb_test"

# Establish a connection
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


# Create a cursor
cursor =conn.cursor()

# Example SQL query
# query = "SELECT * FROM Customers"
sql = "INSERT INTO Customers (CustomerID, FirstName,LastName,Email,PhoneNumber) VALUES (%s, %s,%s, %s,%s)"
val = (4, "Jiji","Gomez",'jiji@gmail.com',46765587)
cursor.execute(sql, val)


# Fetch all results
results = cursor.fetchall()

# Process the results (e.g., print them)
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
