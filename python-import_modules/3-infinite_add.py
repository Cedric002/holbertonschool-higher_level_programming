#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    total = sum(int(arg) for arg in args)
    print("{}".format(total))
