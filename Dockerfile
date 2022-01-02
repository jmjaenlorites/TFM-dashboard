# pull official base image
FROM python:3.8-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
#RUN apt-get update \
 # && apt-get -y install netcat gcc postgresql \
  #&& apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements_docker.txt .
#COPY ./requirements-dev.txt .
RUN pip install -r requirements_docker.txt

# add app
COPY . .

# add entrypoint.sh
#COPY ./entrypoint.sh .
#RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["python"]
CMD ["src/index.py"]