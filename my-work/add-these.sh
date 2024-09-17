#!/bin/bash

echo "Your first number is $1"
echo "Your second number is $2"
echo "lemme add those up real quick..."

SUM=$(( $1 + $2 ))

sleep 3

echo "Your sum is $SUM"

