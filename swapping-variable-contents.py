#!/usr/bin/env python3

# The best way to swap the contents of variables around with one another would be:
# Tuple Unpacking

data0 = 0
data1 = 1

print(data0, data1)

data0, data1 = data1, data0 ## This is Tupple Unpacking, normally tuples have ( ) but it doesn't actually need them, the comma is the most important part

print(data0, data1)