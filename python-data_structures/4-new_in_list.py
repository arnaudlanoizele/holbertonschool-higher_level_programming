#!usr/bin/python3
def new_in_list(my_list, idx, element):
    new_in_list = my_list.copy()
    if 0 <= idx < len(my_list):
        new_in_list[idx] = element
    return new_in_list
