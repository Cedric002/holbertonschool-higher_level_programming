#!/usr/bin/python3
import sys

def main():
    argc = len(sys.argv) - 1
    if argc == 0:
        print("No arguments.")
    elif argc == 1:
        print(f"One argument:")
    else:
        print(f"{argc} arguments:")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
