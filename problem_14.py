"""
14. Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
"""
import pandas as pd

df = pd.read_csv("demo.csv")
header_list = df.columns.values.tolist()

sample_list = []
for i in range (len(df)):
    headers = (list(df.iloc[i].index))
    values = (df.iloc[i].values)
    sample_list.append({})
    for j in range (len(headers)):
        sample_list[i][headers[j]] = values[j]
print(sample_list)
