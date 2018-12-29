#!/bin/bash
N=${1:?count}
NN=${2:?count init}
RT=${3:?runtime}
AC=${4:?action}
OUT=${5:?out}
START=9000
END=$(expr $START + $N - 1)
# killing 
docker ps -q | xargs docker kill
# starting images
seq $START $END | while read port 
do docker run -d -p $port:8080  --name "under-test-$port" --rm $RT
done
# testing
sleep 1
echo "init $(basename $RT) $AC $N" >>$OUT
seq $START $END | xargs /usr/bin/time -p ./multipost -init $AC -run run.dat 2>>$OUT 
sleep 1
# stopping images
seq $(expr $START + 1) $END | while read port 
do docker kill "under-test-$port" 
done
# testing run
echo "run $(basename $RT) $AC $NN" >>$OUT
echo $START | xargs /usr/bin/time -p ./multipost -run run.dat -repeat $NN 2>>$OUT
docker kill under-test-$START
cat $OUT

