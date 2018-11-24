#!/bin/bash
RT=${1:?runtime}
docker run -p8080:8080 -d --name under-test --rm $RT
sleep 2
invoke init main.js
wrk -t1 -c1 -stest.lua http://localhost:8080/run
docker kill under-test
