#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in range(len(str)):
        if ord(str[c]) >= 97 and ord(str[c]) <= 122:
            result += chr(ord(str[c]) - 32)
        else:
            result += str[c]
    print("{}".format(final))
