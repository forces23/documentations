'''
Question 1: 

In a financial portfolio risk management system, n transactions are either gains or losses, represented as integers in the array transactions. You can rearrange the transactions array in any order to maximize the number of transactions during which the portfolio balance stays positive, starting from an initial balance of 0. Implement a function that determines the maximum number of transactions during which the portfolio balance stays above zero. 

The function getMaxPositiveTransactions takes the following input: 
int transactions(n) -> the gains or losses for each transaction 

The function should return the maximum number of transactions during which the portfolio balance stays positive. 

Example :
n = 4 
transactions = [-20, 3, -2]
An optimal transaction order is [3, -2, 1, -20]. The portfolio balance remains positive for the first three transactions, resulting in a balance of 3 - 2 + 1 = 1. It is not possible to process all 4 transactions while keeping the balance positive Hence, the function returns 3. 

'''



from typing import List

def getMaxPositiveTransactions(transactions: List[int]) -> int:
    # Thoughts:
    ## tranactions count needs to stay positive and if not then it should break and return the count
    ## the tranasctions should be ordered in descending oreder so that i can gather a large sum before i start deducting values below 0
    ## Think Greedy 

    transactions.sort(reverse=True)
    trans_count = 0
    balance = 0

    for trans in transactions:
        balance += trans

        if balance <= 0:
            break
        else:
            trans_count+=1
        
    return trans_count


# Test Cases for getMaxPositiveTransactions
print(f"Test Case #1 : {getMaxPositiveTransactions([1, -20, 3, -2])} == 3")
print(f"Test Case #2 : {getMaxPositiveTransactions([5, -2, -1])} == 3")
print(f"Test Case #3 : {getMaxPositiveTransactions([-1, -2, -3])} == 0")
print(f"Test Case #4 : {getMaxPositiveTransactions([10, -5, -4, -3])} == 3")
print(f"Test Case #5 : {getMaxPositiveTransactions([2, 2, 2, -1, -1, -10])} == 5")
print(f"Test Case #6 : {getMaxPositiveTransactions([100])} == 1")
print(f"Test Case #7 : {getMaxPositiveTransactions([-100])} == 0")
print(f"Test Case #8 : {getMaxPositiveTransactions([3, -1, -1, -1, -1])} == 3")
print(f"Test Case #9 : {getMaxPositiveTransactions([1, 2, 3, -10, 5])} == 4")
print(f"Test Case #10 : {getMaxPositiveTransactions([50, -20, -20, -20])} == 3")
print(f"Test Case #11 : {getMaxPositiveTransactions([5, 4, 3, 2, 1])} == 5")
print(f"Test Case #12 : {getMaxPositiveTransactions([-5, 10, -1, -2])} == 4")
print(f"Test Case #13 : {getMaxPositiveTransactions([0, 1, -1])} == 2")
print(f"Test Case #14 : {getMaxPositiveTransactions([7, -3, -3, -3])} == 3")
print(f"Test Case #15 : {getMaxPositiveTransactions([4, -1, -1, -1, -1])} == 4")

