# **Algorithm Patterns**

---



## Prefix Sum

* commonly used when you need to querry the sum of elements in a subarray.

Array =

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| - | - | - | - | - | - | - |

Prefix Sum =

| 1 | 3 | 6 | 10 | 15 | 21 | 28 |
| - | - | - | -- | -- | -- | -- |

P[i] = A[0] + A[0] + ... + A[i]

### LeetCode problems

303. Range Sum Query - Immutable

525. Contiguous Array

560. SubArray Sum Equals K


## Two Pointers *

* its where you have 2 pointers and you move them closer to each other or away from each other.

### LeetCode Problems

167. Two Sum II - Input Array Is Sorted

15. 3Sum

11. Container With Most Water


## Sliding Window *

* allows you to find subarrays or substrings that meet a specific criteria.

### LeetCode Problems

643. Maxium Average Subarray I

3. Longest Substring Without Repeating Characters

76. Minimum Window Substring



## HashMaps (Frequency counting) *

/empty/

## Sorting & Searching *

/empty/


## Fast & Slow Pointers *

* helps solve problems that are related to Linked List and Arrays which involves finding cycles.
* works by moving 2 pointers at different speeds

### LeetCode Problems

141. Linked List Cycle

202. Happy Number

287. Find the Duplicate Number


## Linked List In-place Reversal *

* many linked list problems ask you to change its nodes and pointers in some way
* the trick to this is to do it in place without using any extra space

### Flow

you want to use 3 pointers :

1. previous, current, and next
2. start by setting current to the head of the linked list and set previous to null
3. use a while to go all the way to the end of the linked list and in each loop set next to the next node of the list

### LeetCode Problems

206. Reverse Linked List

92. Reverse Linked List II

24. Swap Nodes in Paris


## Linked List Merging *

/empty/


## Montoic Stack

* uses a stack to find the ext greater or next smaller element in an array

### LeetCode Problems

496. Next Greater Element I

739. Daily Temperature

84. Largest Rectangle in Histogram


## Top 'K' Elements

* this pattern helps find the 'K' largest, 'K' smallest, 'K' most Frequent elements in a data set.

If Question asks to find:

'K' largest ==> Min-Heap

'K' smallest ==> Max-Heap

### LeetCode Problems

215. Kth Largest Element in an Array

347. Top K Frequent Elements

373. Find K Pairs with Smallest Sums


## Overlapping Intervals

* used for word problems involving intervals or ranges that may overlap
* Problem Types you can apply it to:
  1. Merging Intervals
  2. given a collection of intervals merge all overlapping intervals into 1
  3. Interval Intersection
     	find the intersection between 2 sets of intervals.
  4. Insert Interval
     	add a new interval to a none overlaping list of intervals
  5. Find Minimum Meeting Rooms
     	find the minimum number of meeting rooms needed for overlapping meeting times

### LeetCode Problems

56. Merge Intervals

57. Insert Interval

435. Non-overlapping Intervals



## Modified Binary Search

* variant of Binary Search algorithm but its used to solve problems where the array isnt perfectly sorted.

### Use Cases

1. Seaching in a NEARLY SORTED array
2. Seaching in a ROTATED SORTED array
3. Seaching in a list with UNKNOWN LENGTH
4. Searching in an array with DUPLICATES
5. Finding the FIRST OR LAST OCCURENCE of an element
6. Finding the SQUARE ROOT of a number
7. Finding a PEAK element

### LeetCode Problems

33. Search in Rotated Sorted Array

153. Find Minimum in Rotated Sorted Array

240. Search a 2D Matrix II


## Binary Tree Traversal

* this is all about travesing the array in a specific order
* ways to travers the binary tree:
  1. PreOrder: root -> left -> right (easy with recursion)
  2. InOrder: left -> root -> right (easy with recursion)
  3. PostOrder: left -> right -> root (easy with recursion)
  4. LevelOrder: level by level (more difficult)
* better for exploring the tree level by level
* easily implement if using the Q data structure

### use Cases

* To rerieve the values of binary search tree in sorted order, use INORDER TRAVERSAL
* To create a copy of a tree (serialization), use PREORDER TRAVERSAL

* When you want to process child nodes before the parent, use POSTORDER TRAVERSAL
* When you need to explore all nodes at the current level before next, use LEVEL ORDER TRAVERSAL


### LeetCode Problems

257. Binary Tree Paths (PreOrder)

230. Kth Smallest Element in a BST (InOrder)

124. Binary Tree Maximum Path Sum (PostOrder)

107. BinaryTree Level ORder Traversal II (LevelOrder)


## Depth-First Search (DFS) *

* used to explore all paths or branches in trees like :
  * Finding a path between 2 nodes
  * Checking if a graph contains a cylce
  * finding a topological order in a directed acyclic graph (DAG)
  * Counting numbers of a connected componets in a graph

### LeetCode

133. Clone Graph

113. Path Sum II

210. Course Schedule II


## Breadth-First Search (BFS) *

allows you to explore nodes level by level in a tree or graph

### Use cases:

1. Finding thr shorest path between 2 nodes in an unweighted graph
2. printing all nodes of a tree seperatly level by level
3. finding all connect components in a graph
4. finding the shortest transformation sequence from one word to the other

* simple to solve if using a Queue

### LeetCode Problems 

102. Binary Tree Level  Order Traversal

994. Rotting Oranges

127. Word Latter



## Topological Sorting *

/empty/


## Union-Find (Disjoint Set) *



## Matrix Traversal

* Most Matrix traversal problems can be seen as graph problems.
* can use most graph algorithms like DFS and BFS to solve matrix related problems

### Use Case:

1. Finding the shortest path in a grid


### LeetCode Problems

733. Flood Fill

200. Number of Islands

130. Surrounded Regions


## Backtracking

* powerful algorithm for exploring all potential solution paths and backtracking the paths that do not Lead to a valid solution


### Use Cases:

1. Generate all possible permutations combinations of a given set of elements
1. Solve puzzles like Sudoko or N-Queen problems
1. find all possible paths from a start point to a end point in a graph or maze
1. Generate all valid parentheses of a given length (i have seen this before!)
1. Generate all possible subsets


### LeetCode Problems

46. Permutations

78. Subsets

51. N-Queen


## Dynamic Programming (DP) *

* Used for solving optimiszation problems by breaking them down into smaller sub-probmlems and storing their solutions to avoid repetitive work

### Use Cases:

1. Overlapping supbroblems
2. Optimal substructure
   * example: Maximize or minimize a certain value
3. Counting problems
   * example: count the number of ways to acheive a certain goal



### Common DP Patterns

1. Fibonacci Numbers
2. 0/1 Knapsack
3. Longest Common Subsequence (LCS)
4. Longest Increasing SubSequence (LIS)
5. Subset Sum
6. Matrix Chain Multiplication
7. Memoization **
8. Tabulation **

### Memoizaion vs. Tabulation

### LeetCode Problems

70. Climbing Stairs

322. Coin Change

1143. Longest Common Subsequence

300. Longest Increasing Subsequence

416. Partition Equal Subset Sum

312. Burst Ballon

??. Knapsack



## Thread safety, Locks, Deadlocks *

/empty/



## Resources

1. [AlgoMaster](https://algomaster.io/ "Master Patterns, Not Just Problems")
