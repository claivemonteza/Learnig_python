#!/bin/bash

for file in *.HTM;do
    name=$(basename "$file" .HTM)
    mv "$name.html"
done