#!/bin/bash

docker stop money_gone_was

docker rm money_gone_was
docker rm money_gone_data

docker rmi bus3013/money_gone_data:latest
docker rmi bus3013/money_gone_was:latest

rm -rf /home/money_gone_data