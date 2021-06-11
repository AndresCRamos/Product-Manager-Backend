FROM python

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    netcat \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN mkdir ./app
RUN pip install virtualenv
RUN python -m  venv ./venv
RUN ./venv/bin/pip install -r requirements.txt

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8000