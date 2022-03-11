#!/bin/bash

docker container stop $(docker container ls -q --filter name=money_gone*)
docker rm $(docker container ls -q --filter name=money_gone*)
