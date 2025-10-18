'''
Write a function squares_of_evens(nums) that takes a list of integers and returns a new list containing the squares of all even numbers.
'''

from typing import List

def squares_of_evens(nums: List[int]):
    return [num**2 for num in nums if num%2 == 0]

def main():
    print(squares_of_evens([1, 2, 3, 4, 5])) # -> [4, 16]

if __name__ == "__main__":
    main()