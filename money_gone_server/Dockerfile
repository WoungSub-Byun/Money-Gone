FROM python:3.9.10

RUN mkdir -p /app/money_gone

WORKDIR /app/money_gone

RUN mkdir -p /app/money_gone/server

COPY . /app/money_gone/server

RUN pip install -r /app/money_gone/server/requirements.txt

RUN python3 /app/money_gone/server/main.py