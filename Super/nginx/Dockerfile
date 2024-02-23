FROM nginx:latest
RUN rm -f /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/nginx.conf


# /var/www/etc
COPY ssl-super /ssl

RUN mkdir -p /var/www/log

CMD ["nginx","-g","daemon off;","-c","nginx.conf"]
