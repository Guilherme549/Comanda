ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code

ENV SECRET_KEY "bNjyOGox3JJe61dyTAQnaRMQRezVYRxgHC4aNTh3iF7FS7S33L"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Certifique-se de que o gunicorn esteja instalado dentro do contêiner
RUN pip install gunicorn

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "projeto_comanda.wsgi"]

