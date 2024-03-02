FROM python:3.10.12-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app


RUN apt-get update && apt-get upgrade -y && \
    apt-get -y install build-essential python \
                       libpcre3 libpcre3-dev \
                       pkg-config default-libmysqlclient-dev


RUN pip install --upgrade pip && \
    pip install -r requirements.txt



CMD ["bash","./entrypoint.sh"]