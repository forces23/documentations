'''
    🔹 Question 4 — Functions & Clean Code

    Write a function fizzbuzz(n) that prints the numbers from 1 to n, but:

    For multiples of 3 print "Fizz".

    For multiples of 5 print "Buzz".

    For multiples of both, print "FizzBuzz".

    Example:

    fizzbuzz(15)
    # output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
'''
def fizzbuzz(num: int):
    ## im not sure how to make it go in the ascending order using recursive call
    # if num != 0 :
    #     if num % 3 == 0 and num % 5 == 0:
    #         print("FizzBuzz")
    #     elif num % 3 == 0 and num % 5 != 0:
    #         print("Fizz")
    #     elif num % 3 != 0 and num % 5 == 0:
    #         print("Buzz")
    #     else:
    #         print(num)
        
    #     fizzbuzz(num - 1)

    ## using a for loop i can make it go ascending order
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    

print("######## FIZZBUZZ Code #########")
fizzbuzz(15) # output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
print("######## ############# #########")