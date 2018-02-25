#!/bin/bash
prefix="img"
i=0
for File in $1
do
	File=$(echo $File | tr -d \' | tr -d \")
    filename=$(basename $File | tr -d \' | tr -d \")
    extension="${filename##*.}"
    paddedIndex=$(printf "%04d" $i)
    mv $File ${paddedIndex}_${filename}.${extension}
    i=$(($i + 1))
    # notify-send "$File ${paddedIndex}_${filename}.${extension}"
done


# i=0
# for file in $(ls -tr)
# do

# done