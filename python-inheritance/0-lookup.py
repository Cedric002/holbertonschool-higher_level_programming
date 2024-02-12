#!/usr/bin/python3
def lookup(obj):
    attributes_and_methods = dir(obj)
    filtered_list = [attr for attr in attributes_and_methods if not attr.startswith('_')]
    return filtered_list
