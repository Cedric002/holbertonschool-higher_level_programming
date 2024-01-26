#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    addition = 0
    for nb in args:
        addition += int(nb)
print("{}".format(addition))
