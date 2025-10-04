'''
Question 1: 

In a financial portfolio risk management system, n transactions are either gains or losses, represented as integers in the array transactions. You can rearrange the transactions array in any order to maximize the number of transactions during which the portfolio balance stays positive, starting from an initial balance of 0. Implement a function that determines the maximum number of transactions during which the portfolio balance stays above zero. 

The function getMaxPositiveTransactions takes the following input: int transactionsini: the gains or losses for each transaction 

The function should return the maximum number of transactions during which the portfolio balance stays positive. 

Example 
n =4 
transactions = [-20, 3, -2]
An optimal transaction order is [3, -2, 1, -20]. The portfolio balance remains positive for the first three transactions, resulting in a balance of 3 - 2 + 1 = 1. It is not possible to process all 4 transactions while keeping the balance positive Hence, the function returns 3. 

'''



from typing import List

class Solution:
    def getMaxPositiveTransactions(self, transactions: List[int]) -> int:
        # type code here...

    
if __name__ == "__main__":  # entry point
    s = Solution()
    # Test Cases for getMaxPositiveTransactions

print(getMaxPositiveTransactions([1, -20, 3, -2]))        # 3 (3 → 1 → -2 works, -20 breaks it)
print(getMaxPositiveTransactions([5, -2, -1]))            # 3 (5 → 3 → 2, all stay positive)
print(getMaxPositiveTransactions([-1, -2, -3]))           # 0 (balance never goes positive)
print(getMaxPositiveTransactions([10, -5, -4, -3]))       # 3 (10 → 5 → 1, then -2 fails at 4th)
print(getMaxPositiveTransactions([2, 2, 2, -1, -1, -10])) # 5 (2 → 4 → 6 → 5 → 4, then -6 fails)
print(getMaxPositiveTransactions([100]))                  # 1 (single positive stays positive)
print(getMaxPositiveTransactions([-100]))                 # 0 (single negative, balance never > 0)
print(getMaxPositiveTransactions([3, -1, -1, -1, -1]))    # 2 (3 → 2 → 1, then 0 fails at 4th step)
print(getMaxPositiveTransactions([1, 2, 3, -10, 5]))      # 4 (3+2+1=6, -10= -4 fails, so 4 positive steps)
print(getMaxPositiveTransactions([50, -20, -20, -20]))    # 2 (50 → 30 → 10 → -10, fails on last)
print(getMaxPositiveTransactions([5, 4, 3, 2, 1]))        # 5 (all positive, never drops below zero)
print(getMaxPositiveTransactions([-5, 10, -1, -2]))       # 3 (10 → 9 → 7, then -5 would fail if earlier)
print(getMaxPositiveTransactions([0, 1, -1]))             # 1 (0 adds nothing, then +1 works, -1 fails)
print(getMaxPositiveTransactions([7, -3, -3, -3]))        # 3 (7 → 4 → 1 → -2 fails at 4th)
print(getMaxPositiveTransactions([4, -1, -1, -1, -1]))    # 3 (4 → 3 → 2 → 1, then 0 fails at 5th)



