'''
    🔹 Question 2 — Dictionaries & Sets

    You’re given a list of words. Write a function count_unique(words) that returns a dictionary with each unique word as a key and the number of times it appears as the value. Example:

    count_unique(["apple", "banana", "apple", "pear"])  
    # -> {"apple": 2, "banana": 1, "pear": 1}
'''
def count_unique(words: list):
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

    return word_dict

print(count_unique(["apple", "banana", "apple", "pear"]))  # -> {"apple": 2, "banana": 1, "pear": 1}

