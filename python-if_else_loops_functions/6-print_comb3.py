#!/usr/bin/python3
for numbers1 in range(10):
    for numbers2 in range(10):
        if numbers2 == 9 and numbers1 == 8:
            print("{}{}".format(numbers1, numbers2), end="")
        elif (numbers1 != numbers2 and numbers1 < numbers2):
            print("{}{}{}".format(numbers1, numbers2, ", "), end="")
print("")
