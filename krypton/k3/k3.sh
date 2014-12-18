#!/bin/bash

#cipher=$(</games/krypton/krypton2/krypton3)
cipher=$(</Users/sokam/OTW/krypton/k3/krypton3)
alpha=ABCDEFGHIJKLMNOPQRSTUVWXYZ
key=MNOPQRSTUVWXYZABCDEFGHIJKL
echo $cipher | tr $key $alpha
