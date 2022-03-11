FROM python:3.9.10

RUN mkdir -p /money_gone

WORKDIR /money_gone

RUN mkdir -p /money_gone_data

COPY . /money_gone/

RUN pip install -r /money_gone/requirements.txt

RUN python3 main