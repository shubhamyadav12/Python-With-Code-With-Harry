import pandas as pd

data = {
    'Name': ['John', 'Emma', 'Peter', 'Shiva'],
    'Age': [28, 24, 30, 18],
    'City': ['New York', 'San Francisco', 'Chicago', 'India']
}

df = pd.DataFrame(data)
print(df.head())

