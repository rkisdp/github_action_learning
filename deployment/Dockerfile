FROM python:3.8.2-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk --update add \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    # pillow dependencies
    jpeg-dev \
    zlib-dev \
    supervisor \
    gdal-dev \
    geos-dev \
    proj-dev \
    wget \
    tar \
    make \
    nginx \
    nginx-mod-http-headers-more
RUN mkdir /app
RUN mkdir -p /etc/supervisord/conf.d
COPY ./deployment/supervisord.conf /etc/supervisord/supervisord.conf
COPY ./deployment/gunicorn.sh /usr/local/bin/gunicorn.sh
WORKDIR /app
ADD .. /app
RUN pip install --upgrade pip setuptools wheel
RUN pip3 install -r requirements/prod.txt
# nginx conf
RUN mkdir -p /run/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY ./deployment/nginx/nginx.conf /etc/nginx/nginx.conf
RUN chmod +x /usr/local/bin/gunicorn.sh
CMD ["supervisord", "-n", "-c", "/etc/supervisord/supervisord.conf"]