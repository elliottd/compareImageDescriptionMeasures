#!/bin/bash

hypsdir=$1
hyps=(`ls $hypsdir | sort -V`)

refsdir=$2
refs=(`ls $refsdir | grep "\-0\-" | sort -V | cut -b7-`)

let numrefs=$3

len=${#refs[*]}
i=0

pathlen=${#refsdir}-2

refscut=${refsdir:0:$pathlen}

while [ $i -lt $len ]; do
  hypstr=$hypsdir``${hyps[$i]}''
  j=0
  refstr=""
  while [ $j -lt $numrefs ]; do
    refstr="$refstr $refsdir/ref-$j-``${refs[$i]}"
    let j++
  done
  echo $refstr
  python PythonROUGE.py $hypstr $refstr;
  let i++
done
