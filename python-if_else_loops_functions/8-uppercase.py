#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(str[c]) - 32)
        else:
            result += str[c]
    print("{}".format(final))
