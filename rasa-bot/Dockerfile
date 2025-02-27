# ベースイメージ
FROM rasa/rasa:3.5.10

# 作業ディレクトリ
WORKDIR /app

# 必要なファイルをコピー
COPY . /app

# 追加のPythonパッケージをインストール
USER root
# Dockerfile の一部
RUN pip install pydantic<1.10.3
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir ja-ginza

# Rasaのモデルをトレーニング
# RUN rasa train

# ポートの公開
EXPOSE 5005

# Rasaサーバーを起動
CMD ["run", "--enable-api", "--cors", "*"]
