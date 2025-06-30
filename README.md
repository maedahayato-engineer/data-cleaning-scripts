# data-cleaning-scripts

## はじめに
このスプリクト群は、初学者として現場の課題に実践的に取り組む中でのアウトプットです。
未熟ながらも、拡張性を意識し、手を動かしながら学んできました。

## 概要
実務で必要となるCSV・表形式データの前処理スクリプト集です。
欠損値補完や文字コード修正など、現場でありがちな課題を想定して作成しました。
Pythonやpandasを中心に、軽量で再利用性の高いコードを目指しています。

## 使用技術
- Python
- pandas
- chardet

## 主な機能
- 欠損値補完（データ型での最適補完）
- 文字コード変換(UTF-8統一)
- データ型自動変換(予定)
- 一括CSV整形処理(予定)

## 機能①: 欠損値の自動補完
業務でありがちな空白セル（欠損値）をデータ型と歪度から最適な補完をする処理です。
実行には `sample.csv` をルートディレクトリに配置してください（形式例：id, name, score）
- 欠損値処理([`fill_missing_values.py`](./fill_missing_values.py))
 →欠損値(NaN)をデータ型と歪み度合い判断して自動補完する処理を行います。
- 欠損値補完スクリプトの実行
```bash
python3 fill_missing_values.py 
```

## 機能②: 文字コード変換（UTF-8統一）
データ分析現場ではShift_JISやEUC-JPなどのバイナリの違いによる文字化けが発生します。
その前処理として用意しました。
- 文字コード変換([`convert_encoding.py`](./convert_encoding.py))
　→ファイルの文字コードを検出したあと、pandasでUTF-8に統一して書き出す処理です。
- 文字コード変換スクリプトの実行
```bash
python3 convert_encoding.py
```


## 開発環境
- 言語: Python 3.13
- ライブラリ: pandas, chardet
- パッケージ管理: requirements.txt
- エディタ: Visual Studio Code
- OS: macOS


## 環境構築手順

1. 仮想環境の作成(任意)
   Mac / Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   windows:
   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```

2. 依存ライブラリのインストール
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. 実行例
   ```bash
   python3 fill_missing_values.py
   ```


## 学びと今後の展望
- pandasの欠損値処理・データ読み込み方法を学習
- 環境構築・仮想環境・依存管理（requirements.txt）の理解
- 今後は欠損値処理で特徴量選択やKNNなどを加えて、文字変換コードではExcel読み込みへ対応できるよう拡張予定です。