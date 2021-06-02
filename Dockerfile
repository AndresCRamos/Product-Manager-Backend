FROM python

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY requirements.txt .

RUN mkdir ./app
RUN pip install virtualenv
RUN python -m  venv ./venv
RUN ./venv/bin/pip install -r requirements.txt

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8000