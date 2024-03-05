FROM nginx:latest
RUN rm -f /etc/nginx/conf.d/*
COPY nginx/nginx.conf /etc/nginx/conf.d/nginx.conf


# parent以上を参照できないからコピーしてくる
COPY nginx/ssl-super /ssl

RUN mkdir -p /var/www/log && \
    mkdir -p /var/www/html

COPY nginx/favicon.ico /var/www/html/favicon.ico

CMD ["nginx","-g","daemon off;","-c","nginx.conf"]
