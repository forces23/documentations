
'''
    🔹 Question 3 — Strings

    Write a function is_palindrome(s) that checks if a string is a palindrome (same forwards and backwards). Ignore case and spaces. Example:

    is_palindrome("Race car")  # -> True
    is_palindrome("hello")     # -> False
'''
def is_palindrome(s: str):
    # im not sure how to remove " "(spaces) simply which i feel i should be able to. 
    # i guess i could do this 
    # cleaned_str = []
    # alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    # for char in s.lower():
    #     if char in alphabet:
    #         cleaned_str.append(char)

    # cleaned_str = "".join(cleaned_str)

    # i feel i should know how to do regex also but i can think of how to do the full thing all i can think of is 
    # regex = [a-zA-Z] # but this is not an actual the full regex syntax

    # this is the much simpler way i am used to doing it to make it more efficient and more simple
    cleaned_str = "".join(char for char in s if char.isalpha()).lower()

    left, right = 0, len(cleaned_str)-1

    while left < right:
        if cleaned_str[left] != cleaned_str[right]:
            return False
        left+=1
        right-=1

    return True

## instead of doing a while loop and returning true if the while loop finishs the pythonic way would be:
# return cleaned_str == cleaned_str[::-1]


print(is_palindrome("Race car"))  # -> True
print(is_palindrome("hello"))     # -> False
