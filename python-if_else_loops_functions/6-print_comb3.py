#!/usr/bin/python3
for numbers1 in range(10):
    for numbers2 in range(numbers1+1, 10):
        print("{}{},".format(numbers1, numbers2), end=" ")
print()

