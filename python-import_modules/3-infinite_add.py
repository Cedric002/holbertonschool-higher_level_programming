#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    _add = 0
    for nb in args:
        _add += int(nb)
print("{}".format(_add))
