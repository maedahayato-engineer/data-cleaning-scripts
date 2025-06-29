import chardet
import pandas as pd

# ファイル読み込み（自動で文字コード判定）
def detect_encoding(filename):
    with open(filename, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# 文字コード変換関数
def convert_to_utf8(input_file, output_file='converted_sample.csv'):
    encoding = detect_encoding(input_file)
    print(f"Detected encoding: {encoding}")
    
    df = pd.read_csv(input_file, encoding=encoding)
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"File saved as {output_file} with UTF-8 encoding")
# 実行部分
if __name__ == "__main__":
    # 例: sample.csvをUTF-8に変換
    convert_to_utf8("sample.csv")