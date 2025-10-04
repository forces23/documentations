'''
You’re given two sets:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

Write functions that return:

Elements in both sets

Elements in either set but not both

Elements in only a
'''

from typing import Iterable, List

def elements_in_both(a: set, b: set) -> List[int]:
    return [num for num in a if num in b]

def unique_elements(a: set, b: set) -> List[int]:
    # return [num for num in a if num not in a and num not in b]
    uniques_list = []
    for num in a:
        if num not in b:
            uniques_list.append(num)
    
    for num in b:
        if num not in a:
            uniques_list.append(num)

    return uniques_list


def elements_only_in_a(a:set, b:set) -> List[int]:
    return [num for num in a if num not in b]

def main():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    test1 = elements_in_both(set1, set2)
    test2 = unique_elements(set1, set2)
    test3 = elements_only_in_a(set1, set2)

    print(test1)
    print(test2)
    print(test3)

if __name__ == "__main__":
    main()


'''
there was a much more simple way of doing this due to it being set and this way is much more efficient/faster for sets
def elements_in_both(a: set, b: set) -> set:
    return a & b

def unique_elements(a: set, b: set) -> set:
    return a ^ b


def elements_only_in_a(a:set, b:set) -> set:
    return a - b

'''

##############################################
''' 
Here is a Lesson on the Set Operators:
1. "&" → Intersection
    Definition: Returns the set of elements common to both sets.
    Example:
        {1, 2, 3} & {2, 3, 4}  # -> {2, 3}

2. "|" → Union
    Definition: Returns the set of all elements that are in either set (removes duplicates).
    Example:
        {1, 2, 3} | {3, 4, 5}  # -> {1, 2, 3, 4, 5}

3. "-" → Difference
    Definition: Returns the elements that are in the left set but not in the right set.
    Example:
        {1, 2, 3} - {2, 3, 4}  # -> {1}

4. "^" → Symmetric Difference
    Definition: Returns elements that are in exactly one of the sets (excludes intersection).
    Example:
        {1, 2, 3} ^ {3, 4, 5}  # -> {1, 2, 4, 5}
''' 
##############################################