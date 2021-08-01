FROM python:3.8.2-alpine
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
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8000
RUN python manage.py migrate --no-input
RUN python manage.py collectstatic --no-input
CMD python manage.py runserver 0:8000
