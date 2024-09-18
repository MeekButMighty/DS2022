#!/bin/bash

curl -L -o l3bundle.tar.gz https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -xzvf l3bundle.tar.gz 
awk '!/^[[:space:]]*$/' lab3_data.tsv
tr '\t' ',' < lab3_data.tsv > lab3_data.csv
count=$(tail -n +3 lab3_data.csv | wc -l)
echo $count
tar -czvf converted-archive.tar.gz lab3_data.csv


