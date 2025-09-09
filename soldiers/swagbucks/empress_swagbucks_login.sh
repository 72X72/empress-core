#!/data/data/com.termux/files/usr/bin/bash

# EMPRESS Swagbucks Login Injector

source ~/empress/config/swagbucks.env

# Inject credentials into login payload
curl -X POST https://www.swagbucks.com/p/login \
  -d "email=$SWAGBUCKS_EMAIL&password=$SWAGBUCKS_PASSWORD" \
  -c swagbucks_cookies.txt
