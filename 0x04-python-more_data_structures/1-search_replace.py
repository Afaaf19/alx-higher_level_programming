#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [nb if not nb == search else replace for nb in my_list]
