#!/bin/bash
N=${1:?count}
NN=${2:?count init}
RT=${3:?runtime}
AC=${4:?action}
OUT=${5:?out}
START=20000
END=$(expr $START + $N - 1)
ID="$(basename $RT)-$AC"
# starting images
seq $START $END | while read port 
do docker run -d -p $port:8080  --name "under-test-$port" --rm $RT
done
# testing
seq $START $END | xargs time ./multipost -init $AC -run run.dat 2>$ID.init 
echo $START | xargs time ./multipost -run run.dat -repeat $NN 2>$ID.run
echo init-run $(printf "%06d" $N)  $(cat $ID.init) $RT $AC >$OUT
echo only-run $(printf "%06d" $NN)  $(cat $ID.run) $RT $AC>>$OUT
# stopping images
seq $START $END | while read port 
do docker kill "under-test-$port" 
done

