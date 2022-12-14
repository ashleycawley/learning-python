#!/bin/usr/env python3

fruit = ["apple", "pear", "orange"]

for i in range(len(fruit)):     # NOTE: Bad / Non Pythonic:
    print(fruit[i])


for item in fruit:              # NOTE: GOOD / Pythonic:
    print(item)