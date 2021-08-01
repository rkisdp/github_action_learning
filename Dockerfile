FROM python:3.8.5-alpine
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
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

