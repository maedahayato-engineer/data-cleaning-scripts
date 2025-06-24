import pandas as pd

df = pd.read_csv('sample.csv', na_values=["", "NaN", " ", "N/A", "null"])

print("欠損の数:")
print(df.isnull().sum())
print(df)

print(df["age"].apply(lambda x:type(x)))
print(df["age"].unique())

