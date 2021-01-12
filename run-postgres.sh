#!/bin/bash
while (! docker stats --no-stream ); do
    sleep 1
done
docker run --rm -it -p 5432:5432 -e POSTGRES_PASSWORD=test -e POSTGRES_USER=test --name postgres postgres