#!/usr/bin/python3
from calculator_1 import addition, substract, multiply, divide

a = 10
b = 5

print("{} + {} = {}".format(a, b, addition(a, b)))
print("{} - {} = {}".format(a, b, sub(a, subtract)))
print("{} * {} = {}".format(a, b, multiply(a, b)))
print("{} / {} = {}".format(a, b, divide(a, b)))


if __name__ == "__main__":
    main()
