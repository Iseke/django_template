ARG PYTHON_VERSION=3.9.15

### POETRY

FROM python:$PYTHON_VERSION-alpine as poetry

ENV POETRY_VERSION=1.4.1

RUN apk update && \
    apk add --no-cache gcc cargo && \
    apk add --no-cache musl-dev openssl-dev libffi-dev

RUN pip install --no-cache-dir poetry==$POETRY_VERSION

### BUILDER

FROM poetry as builder

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    BUILDER_DIR=/usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR $BUILDER_DIR

RUN apk update && \
    apk add --no-cache jpeg-dev zlib-dev

COPY poetry.lock pyproject.toml ./

RUN poetry export -f requirements.txt --without-hashes $(if [ "$DJANGO_ENV" = "development" ]; then echo "--dev"; fi) --output requirements.txt
RUN pip wheel --no-cache-dir --wheel-dir $BUILDER_DIR/wheels -r requirements.txt

### CLEAN

FROM python:$PYTHON_VERSION-alpine

ARG DJANGO_ENV
ENV DJANGO_ENV=${DJANGO_ENV}

ENV BUILDER_DIR=/usr/src/app \
    WHEELS_DIR=/wheels \
    HOME_DIR=/home/app \
    APP_DIR=/home/app/web \
    SRC_DIR=./application/

RUN addgroup -S app && \
    adduser -S app -G app

RUN mkdir -p $HOME_DIR && \
    mkdir $APP_DIR

RUN mkdir $APP_DIR/run && \
    mkdir $APP_DIR/run/media && \
    mkdir $APP_DIR/run/static

WORKDIR $APP_DIR

COPY --from=builder $BUILDER_DIR/wheels $WHEELS_DIR
COPY --from=builder $BUILDER_DIR/requirements.txt .

RUN pip install --no-cache $WHEELS_DIR/*

COPY $SRC_DIR $APP_DIR

RUN chown -R app:app $APP_DIR
USER app

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
