#!/usr/local/bin/bash

#cipher=$(</games/krypton/kryptoni3/krypton4)

# files
cipher="/Users/sokam/OTW/krypton/k4/krypton4"
found1="/Users/sokam/OTW/krypton/k4/found1"
found2="/Users/sokam/OTW/krypton/k4/found2"
found3="/Users/sokam/OTW/krypton/k4/found3"
declare -a files=("$cipher" "$found1" "$found2" "$found3")

# frequency constants
alphabets=ABCDEFGHIJKLMNOPQRSTUVWXYZ
frequency=ETAOINSHRDLCUMWFGYPBVKJXQZ
singleton=ETAOINSRHLDCUMFPGWYBVKXJQZ
doubleton=("TH" "HE" "IN" "ER" "AN" "RE" "ON" "AT" "EN" "ND" "TI" "ES" "OR" "TE" "OF" "ED" "IS" "IT" "AL" "AR" "ST" "TO" "NT" "NG" "SE" "HA" "AS" "OU" "IO" "LE")
tripleton=("THE" "AND" "ING" "ION" "TIO" "ENT" "ATI" "FOR" "HER" "TER" "HAT" "THA" "ERE" "ATE" "HIS" "CON" "RES" "VER" "ALL" "ONS")
quadraton=("TION" "ATIO" "THAT" "THER" "WITH" "MENT" "IONS" "THIS" "HERE" "FROM")


sub1=""
sub2=""
sub3=""
sub4=""

#declare -A freq=(["A"]=1 ["B"]=2 ["C"]=3) 
declare -A freq=()

function init1 {
	for i in {A..Z} ; do
		freq["$i"]=0
	done
}

function print1 {
	for c in "${!freq[@]}" ; do	
		echo "$c - ${freq["$c"]}"
	done
}

function count1 {
	while read -r -N 1 c ; do
		#echo $c
		if [[ $c =~ ^[A-Z] ]]; then
			let freq["$c"]++
		fi
	done <<< "$1" 

}

function count2 {
	last=$((${#1}-1))
	for i in $(seq 0 $last) ; do
		echo $i
		echo ${1:$i:2}
	done
} 	

function sort1 {
	for k in "${!freq[@]}" ; do
		echo "$k - ${freq["$k"]}"
	done |
	sort -rn -k3
}

function most1 {
	sortoutput=( $(sort1) )

	for i in $(seq 0 3 ${#sortoutput[@]}) ; do
		c=${sortoutput["$i"]}
		if [[ $c =~ ^[A-Z] ]]; then
			sub1+=$c
		fi
	done
}

function printsub1 {
	for f in "${files[@]}" ; do
		echo "---------$f----------------"
		#echo $(cat $f | tr -d " \t\n\r") 
		echo $(cat $f | tr -d " \t\n\r") | tr $sub1 $singleton
	done
}

function main {
	echo "test 1"
	init1
	echo "loop through all files"
	for f in "${files[@]}" ; do
		echo "$f"
		current=$(cat "$f" | tr -d " \t\n\r")
		count1 $current
		count2 $current	
	done
	print1
	echo "Sorted"
	most1
	echo "$sub1"
	printsub1




	#count2 $(cat $found2 | tr -d " \t\n\r")
}

main
