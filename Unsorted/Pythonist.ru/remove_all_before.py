"""
The task is to remove all list elements before given.

Example:
remove_all_before([1, 2, 3, 4, 5], 2) => [2, 3, 4, 5]
remove_all_before([0, 5, 5, 10, 15], 5) => [5, 5, 10, 15]
"""


def remove_all_before(given_list: list, element):
    # in case we are given an empty list
    if not given_list: return []
    for n, el in enumerate(given_list):
        if el == element:
            # if the element is found -> return
            # everything from this index onwards
            return given_list[n:]
    # if the element is not found
    return given_list


print(remove_all_before([], 2))
print(remove_all_before(['a', 'b', 'b', 'c'], 'b'))
print(remove_all_before([0, 1, 2, 3], 6))
print(remove_all_before([0, 2, 4, 6, 8, 10, 10, 12], 8))
