#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    add = 0
    for nb in args:
        add += int(nb)
print("{}".format(add))
