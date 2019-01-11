#!/bin/bash
N=${1:?count}
NN=${2:?count init}
RT=${3:?runtime}
AC=${4:?action}
OUT=${5:?out}
MAIN=${6:-main}
START=9000
END=$(expr $START + $N - 1)
# starting images
seq $START $END | while read port 
do docker run -d -p $port:8080  --name "under-test-$port" --rm $RT
done
# testing
sleep 1
echo "init $RT $AC $N" >>$OUT
seq $START $END | xargs /usr/bin/time -p ./multipost -main "$MAIN" -init $AC -run run.dat 2>>$OUT 
sleep 1
# stopping images
seq $(expr $START + 1) $END | while read port 
do docker kill "under-test-$port" 
done
# testing run
echo "run $RT $AC $NN" >>$OUT
echo $START | xargs /usr/bin/time -p ./multipost -main "$MAIN" -run run.dat -repeat $NN 2>>$OUT
docker kill under-test-$START
cat $OUT

