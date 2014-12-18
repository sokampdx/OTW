#!/bin/bash

cipher=$(</games/krypton/krypton2/krypton3)
alpha=ABCDEFGHIJKLMNOPQRSTUVWXYZ
key=MNOPQRSTUVWXYZABCDEFGHIJKL
echo $cipher | tr $key $alpha
