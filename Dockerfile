FROM python

WORKDIR /code

COPY requirements.txt .

RUN mkdir ./app

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8000