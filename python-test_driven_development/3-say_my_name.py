#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Print "My name is first name and last name"

    first_name and last_name must be strings
    Otherwise: TypeError (first_name must be a string or
                last_name must be a string)

    Returns first_name & last_name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
