#!/bin/bash
RT=${1:?runtime}
AC=${2:?action}
echo "*** Testing $RT ***"
docker run -p8080:8080 -d --name under-test --rm $RT 
echo ""
sleep 2
bash init.sh $AC
wrk -t1 -c1 -stest.lua http://localhost:8080/run
docker kill under-test
