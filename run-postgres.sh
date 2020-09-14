#!/bin/bash
docker run --rm -it -p 5432:5432 -e POSTGRES_PASSWORD=test -e POSTGRES_USER=test --name postgres postgres