# **Greedy Algorithms**

Greedy algorithms are a powerful problem-solving technique where **locally optimal choices** are made at each step to reach a  **globally optimal solution** . They are simple, efficient, and often used in optimization problems.

---

## **1. What is a Greedy Algorithm?**

* **Definition** : A greedy algorithm makes the **best immediate choice** at each step without reconsidering previous decisions.
* **Key Idea** :
* Solve subproblems  **one at a time** .
* Never revisit or undo past choices.
* **When It Works** :
* Problems where  **local optimality leads to global optimality** .
* Problems with the **greedy-choice property** (a global optimum can be reached by selecting local optima).

---

## **2. When to Use a Greedy Approach?**

### **Problem Characteristics**

1. **Optimal Substructure**
   * The problem can be broken into smaller subproblems, and their solutions combine to solve the whole problem.
   * Example: **Shortest path** in a graph (Dijkstra’s algorithm).
2. **Greedy-Choice Property**
   * A globally optimal solution can be achieved by selecting locally optimal choices.
   * Example: **Coin change** (using the fewest coins possible).
3. **No Need for Backtracking**
   * Decisions are final and never reconsidered.
   * Example: **Scheduling jobs** to maximize profit.

### **Common Greedy Problems**

* **Coin Change** (Minimum coins to make change).
* **Fractional Knapsack** (Maximize value with limited weight).
* **Interval Scheduling** (Maximize non-overlapping intervals).
* **Huffman Coding** (Data compression).

---

## **3. How to Identify Greedy Problems in Coding Interviews?**

### **Clues in Problem Statements**

* Keywords:
  * "Maximize" or "minimize" a value.
  * "Shortest," "longest," "earliest," or "latest."
  * "Select the best option at each step."

### **Example Problems**

1. **Coin Change (Greedy Version)**
   * *Problem* : Given coins `[1, 5, 10, 25]`, make change for `30` cents with the fewest coins.
   * *Greedy Choice* : Always pick the largest possible coin first (`25 + 5`).
2. **Activity Selection**
   * *Problem* : Schedule the maximum number of non-overlapping activities.
   * *Greedy Choice* : Always pick the activity with the  **earliest end time** .
3. **Best Time to Buy/Sell Stock II**
   * *Problem* : Buy/sell stocks to maximize profit (multiple transactions allowed).
   * *Greedy Choice* : Sum all increasing price differences (`buy low, sell high`).

---

## **4. Steps to Design a Greedy Algorithm**

1. **Define the Subproblem**
   * Break the problem into steps where a local decision is made.
2. **Identify the Greedy Choice**
   * Determine the best immediate option.
3. **Prove It Works**
   * Show that local choices lead to a global optimum (often the hardest part).
4. **Implement the Algorithm**
   * Iteratively apply the greedy rule.

---

## **5. Example: Coin Change (Greedy)**

### **Problem**

Given coins `[1, 5, 10, 25]`, make `30` cents with the fewest coins.

### **Greedy Approach**

1. **Sort coins in descending order** : `[25, 10, 5, 1]`.
2. **Repeat until remaining amount is `0`:**
   * Take the largest coin ≤ remaining amount.
   * Subtract its value from the total.

### **Solution**

* `30 - 25 = 5` → Use `25¢`.
* `5 - 5 = 0` → Use `5¢`.
* **Total coins** : `2` (`25 + 5`).

### **Code**

```javascript
function coinChange(coins, amount) {
    coins.sort((a, b) => b - a); // Sort descending
    let count = 0;
    for (const coin of coins) {
        while (amount >= coin) {
            amount -= coin;
            count++;
        }
    }
    return amount === 0 ? count : -1; // -1 if no solution
}
```

 **Note** : This works only for certain coin systems (e.g., US coins). Fails for `coins = [1, 3, 4]`, `amount = 6` (greedy gives `4 + 1 + 1 = 3 coins`, but optimal is `3 + 3 = 2 coins`).

---

## **6. Pros and Cons of Greedy Algorithms**

| **Pros**                                         | **Cons**                        |
| ------------------------------------------------------ | ------------------------------------- |
| Fast and simple to implement.                          | Doesn’t always guarantee optimality. |
| Often runs in**O(n log n)** or  **O(n)** . | Requires proof of correctness.        |
| Low memory usage (**O(1)** space).               | Limited to specific problems.         |

---

## **7. How to Prove a Greedy Algorithm Works**

### **Two Key Proof Techniques**

1. **Greedy Stays Ahead**
   * Show that the greedy choice is never worse than alternatives.
   * Example: **Interval Scheduling** (selecting earliest end time always leaves maximum remaining time).
2. **Exchange Argument**
   * Compare the greedy solution to an optimal one and show they must be equivalent.
   * Example: **Fractional Knapsack** (swapping items doesn’t improve the solution).


## **8. Practice Problems**

### **Easy**

* [Best Time to Buy/Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
* [Assign Cookies](https://leetcode.com/problems/assign-cookies/)

### **Medium**

* [Jump Game](https://leetcode.com/problems/jump-game/)
* [Gas Station](https://leetcode.com/problems/gas-station/)

### **Hard**

* [Candy](https://leetcode.com/problems/candy/)
* [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
