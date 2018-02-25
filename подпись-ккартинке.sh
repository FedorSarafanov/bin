#!/usr/bin/bash

for f in ex_9_fed.png
do
  echo "Processing $f file..."
  fil=`basename $f`
  title=`basename $f .png`
  echo $fil
  convert $fil -gravity south -undercolor black -fill yellow -font courier -pointsize 15 -annotate +0+0 "$title" out/$fil
  # take action on each file. $f store current file name
  # cat $f
done