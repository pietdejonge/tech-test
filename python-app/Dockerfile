FROM python:2.7

MAINTAINER Sushan Ghimire

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

## build and run
# docker build -t python-app:latest .
# docker run -p 5000:5000 --name myapp -d python-app