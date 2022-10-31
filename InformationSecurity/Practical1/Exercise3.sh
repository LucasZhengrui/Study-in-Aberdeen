#!/bin/bash
# Find the biggest number in these three num
max=0
number=3
echo "Enter three Numbers"
for i in 1 2 3;
do
  read num
  if [ $num -gt $max ]
  then
      max=$num
  fi
  i=$((i+1))
done
echo "The biggest one is: $max"
