# ベースイメージ
FROM python:3.11

# 作業ディレクトリ
WORKDIR /app

# 必要なファイルをコピー
COPY . /app

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# Gunicornでアプリを起動
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
