'''
    Problem #3 – Word Frequency Counter

    Write a function word_count that takes in a string and returns a dictionary where the keys are words and the values are how many times each word appears.

    Example:
    word_count("the cat and the hat")
    # -> {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}


    👉 This is a dictionary trick because you’ll need to use:

    .get(key, default) to avoid KeyErrors, or

    collections.defaultdict(int) to simplify counting, or

    collections.Counter for a super clean solution.
'''

from collections import Counter, defaultdict
from typing import List


def word_counter_counter(s: str) -> dict:
    words = s.split(" ")

    word_count = Counter(words) 
    
    return word_count

def word_counter_get(s: str) -> dict:
    word_count = {}
    words = s.split(" ")

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def word_counter_defaultdict(s: str) -> dict:
    words = s.split(" ")
    word_count = defaultdict(int)

    for word in words:
        word_count[word] += 1
    
    return word_count


def main():
    test1 = word_counter_counter("the cat and the hat")
    test2 = word_counter_get("the cat and the hat")
    test3 = word_counter_defaultdict("the cat and the hat")

    print(test1)
    print(test2)
    print(test3)
    print()

    # all can be access like nirmal dictionaries 
    print(test1["the"])
    print(test2["cat"])
    print(test3["hat"])
    print()

    # the only concern i seen was that for defaultdict it will create a new inset in the dict. that can be dangerous if you did want to do this 
    print(test1["a"]) # Counter will return 0 for missing keys (and adds the key into the dict).
    print("test2 will cause an error due to key not existing")
    # print(test2["a"]) # this will cause an error due to key not existing
    print(test3["a"]) # this will create a new insert in the dictionary with a default value of 0
    print()

    # NOTE: counter works similarly to defaultdict BUT Counter only returns 0 temporarily when missing, and won’t actually insert until you perform an update/assignment.

    print(test1)
    print(test2)
    print(test3)

    
    
    
    

if __name__ == "__main__":
    main()




    