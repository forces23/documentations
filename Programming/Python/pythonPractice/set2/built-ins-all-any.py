'''
    Write a function `all_positive(nums)` that returns `True` if all numbers in a list are > 0.
'''
from typing import List

def all_positive(nums:List[int]) -> bool:
    return all(num > 0 for num in nums)

def any_below_1(nums:List[int]) -> bool:
    return  not any(num < 1 for num in nums)
    
def main():
    print("Using all():")
    print(all_positive([1,2,3,4,5]))
    print(all_positive([1,2,-3,4,-5]))
    print(all_positive([-1,-3]))
    print(all_positive([1,0,3]))

    print("")
    print("Using any():")
    print(any_below_1([1,2,3,4,5]))
    print(any_below_1([1,2,-3,4,-5]))
    print(any_below_1([-1,-3]))
    print(any_below_1([1,0,3]))


if __name__ == "__main__":
    main()