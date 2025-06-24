# data-cleaning-scripts

## 概要
実務で必要となるCSV・表形式データの前処理スクリプト集です。
欠損値補完や文字コード修正など、現場でありがちな課題を想定して作成しました。
Pythonやpanadasを中心に、軽量で再利用性の高いコードを目指しています。

## 使用技術
- Python
- pandas
- chardet

## 主な機能
- 欠損値補完（平均値・中央値補完）
- 文字コード変換(UFT-8統一)
- データ型自動変換
- 一括CSV整形処理

## 機能①: 欠損値の自動補完
業務でありがちな空白セル（欠損値）を平均や中央値で自動補完する処理です。
実行には `sample.csv` をルートディレクトリに配置してください（形式例：id, name, score）
- 欠損値処理([`fill_missing_values.py'](./fill_missing_values.py))
 →欠損値(NaN)を平均値または中央値で自動補完する処理を行います。
# 欠損値補完スクリプトの実行
python3 fill_missing_values.py 

## 機能②: 文字コード変換（UFT-8統一）
処理の説明（後述）
実行には`sample.csv`をルートディレクトリに配置してください
# 文字コード変換スクリプトの実行
python3 （後述）
- 文字コード変換([`後述`](./後述))

## 開発環境
- 言語: Python 3.13
- ライブラリ: pandas, chardet
- パッケージ管理: requirements.txt
- エディタ: Visual Studio Code
- OS: macOS

```md
## 環境構築手順

1. 仮想環境の作成(任意)
   Mac / Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

   windows:
   python3 -m venv venv
   venv\Scripts\activate

2. 依存ライブラリのインストール
   python3 -m pip install -r requirements.txt

3. 実行例
   python3 fill_missing_values.py


## 学びと今後の展望
- pandasの欠損値処理・データ読み込み方法を学習
- 環境構築・仮想環境・依存管理（requirements.txt）の理解
- 今後は文字コード処理や、Excelファイル対応にも拡張予定