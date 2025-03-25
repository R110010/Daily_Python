 # Read a CSV file and extract specific columns.
import pandas as pd
df = pd.read_csv("my_csv.csv")
select = df[["Name","Age"]]
print(select)
print(df)