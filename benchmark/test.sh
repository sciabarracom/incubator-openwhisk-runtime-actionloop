#!/bin/bash
N=${1:?count}
NN=${2:?count init}
RT=${3:?runtime}
AC=${4:?action}
OUT=${5:?out}
START=20000
END=$(expr $START + $N - 1)
# starting images
seq $START $END | while read port 
do docker run -d -p $port:8080  --name "under-test-$port" --rm $RT
done
# testing
sleep 1
echo "init $(basename $RT) $AC $N" >>$OUT
seq $START $END | xargs time ./multipost -init $AC -run run.dat 2>>$OUT 
sleep 1
# stopping images
seq $(expr $START + 1) $END | while read port 
do docker kill "under-test-$port" 
done
# testing run
echo "run $(basename $RT) $AC $NN" >>$OUT
echo $START | xargs time ./multipost -run run.dat -repeat $NN 2>>$OUT
docker kill under-test-$START
#INIT=$(awk '{print $1}' <$ID.init)
#RUN=$(awk '{print $1}' <$ID.run)
#echo  $(printf "%05d init %05.2f" $N $INIT) $RT $AC >>$OUT
#echo  $(printf "%05d run_ %05.2f" $NN $RUN) $RT $AC>>$OUT
cat $OUT

