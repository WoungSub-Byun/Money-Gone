#!/bin/bash

docker run -d -v /home/money_gone_data:/data --name "money_gone_data" bus3013/money_gone_data:latest
docker run -d -p 80:8080 -v /home/money_gone_data:/money_gone/templates --name "money_gone_was" bus3013/money_gone_was:latest