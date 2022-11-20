#!/bin/zsh
# 1/A 1234567890 Levent Aydinbakar

mkdir -p shell1
cd shell1

for i in {1..3}
do
  for j in {1..11}
  do
    mkdir -p ${i}/$(printf %04d ${j})
    for k in {1..101}
    do
      touch ${i}/$(printf %04d ${j})/$(printf %04d ${k}).txt
      echo "This is ${k}th file in ${i}/$(printf %04d ${j})." >> ${i}/$(printf %04d ${j})/$(printf %04d ${k}).txt
    done
  done
done
