![1756323308721](image/ComputerScience&PrgrammingFundamentals/1756323308721.png)

# Programming Fundamental

## Variables, Data Types, and Operators

### **Variables** 

Variable is a label box where you can store data for later use.

* the name of this box should represent what is actually being stored in it.

```java
// Java
int age = 25;       // stores an integer
String name = "Bobby"; // stores text
double height = 6.0;   // stores a decimal number

```

```ts
// Typescript 
let age: number = 25;
let name: string = "Bobby";
let height: number = 6.0;

```

### Data Types 

Data Types define what kind of value a variable can hold

* Common Types of Data Types:

| Java           | Typescript | Defined As                                                                | Examples                     | Constraints |
| -------------- | ---------- | ------------------------------------------------------------------------- | ---------------------------- | ----------- |
| integer        | number     | Whole Numbers                                                             | 1, 100, -80, -10             |             |
| Floating point | decimal    | Numbers with decimals                                                     | 1.1, 10.99, -100.0           |             |
| String         | String     | Text                                                                      | "Hello world"                |             |
| Boolean        | Boolean    | True or False                                                             | true, false                  |             |
| Array          | List       | A Collections of items                                                    | [1,2,3,4] , ["a", "b", "c"]  |             |
| Object         | Object     | A structured collection of properties <br />and values -- key, value pair | {"name": "Bobby", "age": 30} |             |

### Operators

#### Arithmetic

| Operator | Name     | Defined                                                                                                                                                                                                                                                         |
| -------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +        | Add      | add/combines 2 values together                                                                                                                                                                                                                                  |
| -        | Subtract | subtracts values                                                                                                                                                                                                                                                |
| *        | Multiply | Multiplies values                                                                                                                                                                                                                                               |
| /        | Divide   | Divides values                                                                                                                                                                                                                                                  |
| %        | Modulus  | takes 2 numbers and outputs the remainder<br />Example to find even numbers you would take a number (4) and use % 2 <br />to see if the remainder is 0. if its 0 then it is even if it is not then it is odd<br />`if (4%2 == 0) {system.out.pintln("even")}` |

#### Comparison

| Operator                        | Name                     | Defined                                                                                                                                                                                                                           |
| ------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `==` (java)<br />`===` (ts) | compare                  | checks to see if 2 values are the same<br />`1 == 2 // returns false`<br />`"Apples" == "Apples" // returns true`<br /><br />`==` is somthing you should not use in TS. The comparison works differently in TS with `==` |
| `!=` (java)<br />`!==` (ts) | does not Compare         | Checks to see if 2 values are not a match<br />`5 != 5 // returns false`<br />`"Hello" != "hello" // returns true`                                                                                                            |
| `>`                           | greater than             | this compares numbers  to see if one is less than the other<br />`1<2 // return true`<br />`3<1 // return false`<br />`1<1 // return false`                                                                                |
| `<`                           | less than                | this compares numbers  to see if one is greater than the other<br />`1>2 // return false`<br />`3>1 // return true`<br />`1>1 // return false`                                                                             |
| >=                              | greater than or equal to | this compares numbers  to see if one is less than or equal to the other<br />`1>=1 // return true`                                                                                                                             |
| `<=`                          | less than or equal to    | this compares numbers  to see if one is greater than or equal to the other<br />`1<=1 // return true`                                                                                                                         |

#### Logical

| col1   | col2 | col3                                   |
| ------ | ---- | -------------------------------------- |
| `&&` | AND  | both have to be true to pass           |
| `\|\|` | OR   | 1 or the other have to be true to pass |
| `!`  | NOT  | negates whatever you add this to       |

#### Assignment

| Operator | Name                           | Defined                                                                                                                                                          |
| -------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| =        | asignment                      | `int a = 3;`                                                                                                                                                   |
| +=       | incrment<br />assignment       | `a += 3 // since a was 3 and i just incremented by 3 a is now 6`<br /><br />to show what this is actually doing this is the same as above <br />`a = a + 3` |
| -=       | decrement<br />assignment      | `a -= 2 // a now equals 4`                                                                                                                                     |
| *=       | multiplication<br />assignment | `a *= 2 // a now is 8`                                                                                                                                         |
| /=       | division<br />assignment      | `a /= 4 // a now is 2`                                                                                                                                         |


## Control Flow (if/else, switch, loops)

## Functions (parameters, return values, scope)

## Recursion (when & why to use it)

## Error Handling & Exceptions

## Input/Output (file handling, streams)

# Data Structures

* Arrays & Strings
* Linked Lists (singly, doubly, circular)
* Stacks & Queues (including priority queues)
* Hash Tables / Hash Maps
* Trees (binary trees, BST, heaps, tries)
* Graphs (representation, BFS, DFS, shortest paths)

# Algorithms

* Sorting (bubble, insertion, merge, quick, heap)
* Searching (linear, binary, graph traversals)
* Divide & Conquer (merge sort, quick sort)
* Greedy Algorithms (Huffman coding, scheduling)
* Dynamic Programming (Fibonacci, knapsack, longest common subsequence)
* Backtracking (N-Queens, subset sum)
* Big-O Notation (time & space complexity)

# Object-Oriented Programming (OOP)

* Classes & Objects
* Encapsulation, Inheritance, Polymorphism, Abstraction
* Interfaces vs Abstract Classes
* Design Principles (SOLID)
* Common Design Patterns (Singleton, Factory, Observer, Strategy)

# Databases

* Relational Databases (SQL basics: SELECT, JOINs, indexes)
* NoSQL (key-value, document-based, columnar, graph DBs)
* Transactions, ACID properties
* Normalization vs Denormalization

# Operating Systems

* Processes vs Threads
* Concurrency & Synchronization (locks, semaphores, deadlocks)
* Memory Management (stack vs heap, paging, virtual memory)
* File Systems
* CPU Scheduling basics

# Networking Basics

* OSI Model (7 layers)
* TCP vs UDP
* IP addressing, DNS, HTTP/HTTPS
* Sockets & APIs

# Sofware Engineering Practices

* Version Control (Git basics: clone, branch, merge, rebase)
* Testing (unit testing, integration testing, test-driven development)
* Agile vs Waterfall methodologies
* Continuous Integration / Continuous Deployment (CI/CD) basics

# Security Fundamentals

* Encryption (symmetric vs asymmetric)
* Hashing (MD5, SHA, bcrypt)
* Authentication vs Authorization
* Common vulnerabilities (SQL injection, XSS, CSRF)

# Advanced / Nice-to-Have

* Functional Programming Concepts (immutability, pure functions, map/reduce/filter)
* Multithreading & Parallel Programming
* Compiler Basics (lexical analysis, parsing)
* Cloud Fundamentals (AWS, Azure, GCP basics)
