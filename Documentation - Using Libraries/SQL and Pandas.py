'''This educational script illustrates the use of SQL operations with pandas.

It covers:
- Creating an in-memory SQLite database
- Writing a DataFrame to a SQL database
- Reading data from a SQL database using different methods
'''


import pandas as pd
from sqlalchemy import create_engine

# Create an in-memory SQLite database
engine = create_engine('sqlite:///:memory:') # change to 'sqlite:///path/to/database.db' to use a file-based database

# Create sample data
sample_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28]
})

# Write DataFrame to SQL database
sample_df.to_sql('employees', engine, index=False, if_exists='replace')

# Read data from SQL using different methods
# Method 1: Read entire table
sql_df1 = pd.read_sql_table('employees', engine)

# Method 2: Read with custom SQL query
sql_df2 = pd.read_sql_query('SELECT * FROM employees WHERE age > 30', engine)

# Method 3: Read with simplified syntax
sql_df3 = pd.read_sql('SELECT name, age FROM employees ORDER BY age DESC', engine)

# Print results
print("All employees:")
print(sql_df1)
print("\nEmployees over 30:")
print(sql_df2)
print("\nNames and ages sorted:")
print(sql_df3)