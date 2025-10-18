'''
    🔹 Question 1 — Lists & Loops

    Write a function remove_even(nums) that takes a list of integers and returns a new list with all even numbers removed. Example:

    remove_even([1,2,3,4,5,6])  # -> [1,3,5]
'''
def remove_even(nums: list): ## needed to specify the element type for list -> List[int]
    # odds_only_list = []

    # for num in nums:
    #     if num % 2 != 0:
    #         odds_only_list.append(num)
    
    # return odds_only_list

    ## instead of doing the above the pythonic way is like this:
    return [num for num in nums if num%2 != 0]

print(remove_even([1,2,3,4,5,6]))  # -> [1,3,5]

