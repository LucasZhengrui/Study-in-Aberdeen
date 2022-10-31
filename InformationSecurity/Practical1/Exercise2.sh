#!/bin/bash
# Here is a script to rename all of the files in the folder, to be specific, it will add a number to every filename.
i=1
for f in $( ls . ); do
    echo We found the following file: $f
    name=$f" "$i
    echo $name
    i=$(($i+1))
done  
