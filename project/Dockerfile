###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.11-slim-buster as builder

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install python dependencies
RUN pip install --upgrade pip
COPY requirements_docker.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements_docker.txt

# lint
COPY . /usr/src/app/
RUN pip install black==21.6b0 flake8==3.9.2 isort==5.9.1
RUN flake8 .
RUN black --exclude=migrations .
RUN isort .


#########
# FINAL #
#########

# pull official base image
FROM python:3.8.11-slim-buster

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0
ENV PORT 8050

# install python dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements_docker.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*
#RUN pip install "uvicorn[standard]==0.14.0"

# add app
COPY . .

# chown all the files to the app user
RUN chown -R app:app $HOME

# change to the app user
USER app


ENTRYPOINT ["python"]
CMD ["app/index.py"]