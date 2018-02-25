#!/usr/bin/bash
for file in $(ls -t */*.pdf); do
	name=$(echo $file | sed 's/\..*$//')
	# convert -density 300 -alpha remove $name.pdf $name.jpg
	echo $path -- сконвертирован
	pdf=$(basename $file);
	f=$(basename -s .pdf $file);
	PageCount=$(pdfinfo $file | grep Pages | awk '{print $2}');
	echo $f;
	# echo $PageCount;
	for ((i=0; i < $PageCount; i++))
	do
		echo $f-$i.jpg
	done
done

