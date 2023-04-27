FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN mkdir /app/staticfiles

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
