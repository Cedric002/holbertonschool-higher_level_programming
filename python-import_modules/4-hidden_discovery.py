#!/usr/bin/python3
import hidden_4

def main():
    for name in dir(hidden_4):
        if not name.startswith("__"):
            print("{}".format(name))

if __name__ == "__main__":
    main()
