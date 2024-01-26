#!/usr/bin/python3
from calculator_1 import addition, subtraction, multiply, divide

def main():
    a = 10
    b = 5

    print("{} + {}".format(addition(a, b)))
    print("{} - {}".format(subtraction(a, b)))
    print("{} * {}".format(multiply(a, b)))
    print("{} / {}".format(divide(a, b)))

if __name__ == "__main__":
    main()
