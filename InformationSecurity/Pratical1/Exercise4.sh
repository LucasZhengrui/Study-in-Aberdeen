#!/bin/bash
# Write a simple calculator that takes three commandline arguments:
# Argument $1 : a number
# Argument $2 : an arithmetic operator, + - / *
# Argument $3 : a number

echo "Please input three arguments to calculate 1 (2) 3, 2 is an arithmetic operator(e.g + - / *)"
read arg1 arg2 arg3
echo $arg1 $arg2 $arg3
case $arg2 in
    "+") result=$(($arg1+$arg3)) ;;
    "-") result=$(($arg1-$arg3)) ;;
    "*") result=$(($arg1*$arg3)) ;;
    "/") result=$(($arg1/$arg3)) ;;
esac
echo $result # print the result
