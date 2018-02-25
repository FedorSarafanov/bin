#!/bin/bash
# prefix="img"
# i=0
for File in $1
do
	File=$(echo $File | tr -d \' | tr -d \")
	if [[ "$File" == *\.tex ]]
	then
		# if [[ "$File" == *img\.tex ]]
		# then
		# echo false
		# else
    	latexmk -cd -f -pdf -interaction=nonstopmode -synctex=1 $File &&
    	notify-send -t 80 "$File скомпилирован"
		# fi
	    # echo true
	else
	    echo false
	fi
    # filename=$(basename $File | tr -d \' | tr -d \")
    # extension="${filename##*.}"
    # paddedIndex=$(printf "%04d" $i)
    # mv $File ${paddedIndex}_${filename}.${extension}
    # i=$(($i + 1))
done

cd $2

rm *.fls
rm *.fdb_latexmk
rm *.aux
rm *.log
rm *.synctex.gz
rm *.snm
rm *.toc
rm *.nav
rm *.out

notify-send -t 150 "Временные файлы успешно удалены"


# i=0
# for file in $(ls -tr)
# do

# done