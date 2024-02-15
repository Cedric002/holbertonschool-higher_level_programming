#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "read", encoding="utf-8") as filee:
        for line in filee:
            print(line, end='')
