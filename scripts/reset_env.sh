#!/bin/bash

docker stop money_gone_was

docker rm money_gone_was
docker rm money_gone_data

rm -rf /home/money_gone_data