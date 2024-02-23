FROM python:3.11.8-bullseye

ARG UID=1000
ARG GID=1000

# 新しいユーザーとグループを作成
RUN groupadd -g $GID appuser && \
    useradd -m -u $UID -g appuser appuser
# 作成したユーザーに切り替え
USER appuser

# 作業ディレクトリの設定
WORKDIR /code

# RUN apt-get update && apt-get upgrade -y && \
#     apt-get -y install build-essential python \
#                         libpcre3 libpcre3-dev \
#                         pkg-config default-libmysqlclient-dev

# アプリケーションの依存関係をインストール
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# RUN mkdir /app/tmp/sockets/ -p && \
#     touch /app/tmp/sockets/app.sock


COPY . .

# RUN python3 manage.py makemigrations && \
#     python3 manage.py migrate && \
#     python3 manage.py collectstatic

# COPY uwsgi.ini .
# CMD ["uwsgi","--ini","uwsgi.ini"]


CMD ["/bin/bash"]