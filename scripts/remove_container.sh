#!/bin/bash

docker container stop $(docker container ls -q --filter name=money_gone*)
docker rm bus3013/money_gone:latest
