import pandas as pd

df = pd.read_csv('sample.csv',na_values=["", " ", "NAN", "NaN"])  # 例: 欠損ありCSV
print("欠損の数:")
print(df.isnull().sum())

# 平均で埋める（数値だけ）
df_filled = df.fillna(df.mean(numeric_only=True))

# 保存
df_filled.to_csv('cleaned_sample.csv', index=False)