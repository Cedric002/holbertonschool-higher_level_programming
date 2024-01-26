#!/usr/bin/python3
import sys

args = sys.argv[1:]
addition = 0
for nb in args:
    addition += int(nb)
print("{}".format(addition))

if __name__ == "__main__":
