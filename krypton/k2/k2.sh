#!/bin/bash

cipher=$(</games/krypton/krypton1/krypton2)
alpha=ABCDEFGHIJKLMNOPQRSTUVWXYZ
echo $alpha
echo $cipher

fst=${alpha:0:13}
snd=${alpha:13:13}
rot=$snd$fst

echo $rot
echo $cipher | tr $alpha $rot


