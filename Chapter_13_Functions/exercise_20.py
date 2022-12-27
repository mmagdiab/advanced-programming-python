"""
Write a function called merge that takes two already sorted lists of possibly different lengths,
and merges them into a single sorted list.
(a) Do this using the sort method.
(b) Do this without using the sort method.
"""


def merge_a(list_1, list_2):
    big_list = list_1 + list_2
    big_list.sort()
    return big_list


def merge_b(list_1, list_2):
    big_list = []
    list_1_pointer = 0
    list_2_pointer = 0

    while list_1_pointer < len(list_1) and list_2_pointer < len(list_2):
        if list_1[list_1_pointer] <= list_2[list_2_pointer]:
            big_list.append(list_1[list_1_pointer])
            list_1_pointer += 1
        else:
            big_list.append(list_2[list_2_pointer])
            list_2_pointer += 1

    # Append the remainder of the shortest list
    if list_1_pointer < len(list_1):
        big_list = big_list + list_1[list_1_pointer:]

    if list_2_pointer < len(list_2):
        big_list = big_list + list_2[list_2_pointer:]

    return big_list



