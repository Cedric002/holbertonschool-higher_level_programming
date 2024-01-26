#!/usr/bin/python3
import sys

def main():
    addition = 0
    for nb in range(1, len(sys.argv)):
        addition += int(sys.argv[nb])
    print("{}".format(addition))

if __name__ == "__main__":
    main()
