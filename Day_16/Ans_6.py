#Write data to a CSV file.
import pandas as pd
new_data = {
    "Name":["Sunil"],
    "Age":[27],
    "City":["Thimpu"]
}
df = pd.DataFrame(new_data)
df.to_csv("my_csv.csv",mode='a',header=False, index=False)
print(" new data written to csv ")