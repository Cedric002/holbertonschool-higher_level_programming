#!/usr/bin/python3
for alphabets in range(97, 123):
    if not (alphabets == 101 or alphabets == 113):
        print("{}".format(chr(alphabets)), end="")
