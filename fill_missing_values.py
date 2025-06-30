import pandas as pd

class DataCleaner:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    # 欠損値をデータ型ごとに最適な方法で補完する関数
    def fill_missing_values(self):

        self.df = pd.read_csv(self.input_file, na_values=["", " ", "NAN", "NaN"])
        print('欠損数：')
        # columns毎の欠損数を表示
        print(self.df.isnull().sum())

        for col in self.df.columns:
            # 欠損値がない場合はスキップ
            if self.df[col].isnull().sum() == 0 :
                continue
            # 数値型の列は歪みを確認して補完方法を決定
            if pd.api.types.is_numeric_dtype(self.df[col]):
                skew = self.df[col].skew()
                if skew < -1 or skew >1:
                    # 歪みが多いなら中央値で埋める
                    self.df[col] = self.df[col].fillna(self.df[col].median())
                else:
                    # 正規分布っぽいなら平均で
                    self.df[col] = self.df[col].fillna(self.df[col].mean())

            # 日付型は最頻値で埋める
            elif pd.api.types.is_datetime64_any_dtype(self.df[col]):
                self.df[col] = self.df[col].fillna(self.df[col].mode().iloc[0])

             # カテゴリ・文字列型は最頻値で埋める
            elif pd.api.types.is_categorical_dtype(self.df[col]) or self.df[col].dtype == object:
                if not self.df[col].mode().empty:
                    self.df[col] = self.df[col].fillna(self.df[col].mode().iloc[0])
                # 最頻値がない場合は『不明』で埋める
                else:
                    self.df[col] = self.df[col].fillna("不明")

    def save_cleaned_data(self):
        # 補完後のデータを保存
        self.df.to_csv(self.output_file, index=False)











    
