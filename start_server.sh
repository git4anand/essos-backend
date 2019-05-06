#!/bin/sh

git pull
docker build -t essos_backend .
docker stop essos
docker rm essos
docker run -d -p 80:80 --name essos essos_backend
