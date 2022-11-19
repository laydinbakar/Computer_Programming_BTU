#!/bin/zsh
# 1234567890 Levent Aydinbakar

f1=$1
f2=$2
f3=$3

mkdir -p shell2

for i in $f1 $f2 $f3
do
  for j in {1..13}
  do
    mkdir -p shell2/${i}/$(printf %04d ${j})
    for ((k=20; k<=115; k=${k}+5))
    do
      touch shell2/${i}/$(printf %04d ${j})/$(printf %03d ${k}).txt
	  if [[ $(python3 -c "print(${k}%2)") == 0 ]]
	  then
        echo "This is an even file." >> shell2/${i}/$(printf %04d ${j})/$(printf %03d ${k}).txt
	  else
        echo "This is an odd file." >> shell2/${i}/$(printf %04d ${j})/$(printf %03d ${k}).txt
      fi
    done
  done
done
