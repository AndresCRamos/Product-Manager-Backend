FROM python

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8000