# ベースイメージ
FROM python:3.10

# 作業ディレクトリ
WORKDIR /app

# ファイルをコンテナ内にコピー
COPY . /app

# 権限の設定
USER root

# pip のアップグレードを追加
RUN pip install --upgrade pip

# 必要なパッケージをインストール
RUN pip install -r requirements.txt

# ja-ginza のインストール
RUN pip install --no-cache-dir ja-ginza

# ポートを開放
EXPOSE 5005

# Rasa の起動コマンド
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
