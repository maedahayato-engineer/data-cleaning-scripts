import chardet
import pandas as pd

def detect_encoding(filename):
    with open(filname, 'rb') as f:
        resulut = chardet.detect(f.read())
    return resulut['encoding']

def convert_to_utf8(input_file, output_file='converted_sample.csv'):
    encoding = detect_encoding(input_file)
    print(f"Detected encoding: {encoding}")
    
    df = pd.read_csv(input_file, encoding=encoding)
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"File saved as {output_file} with UTF-8 encoding")

if __name__ == "__main__":
    # 固定ファイル名（変更してもOK）
    convert_to_utf8("sample.csv")