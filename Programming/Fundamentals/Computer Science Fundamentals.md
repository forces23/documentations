ser![1756771221951](image/ComputerScienceFundamentals/1756771221951.png)

# Big-O Notation

**What is Big-O?**

It is a way to describe how an algorithm scales as input size(`n`) grows

Big-O focuses on the worst-case scenario (most commonly asked in interviews)

It ignores constants and small terms (we care about growht trends, not exact operations)

**Comon Complexities**

**O(1) - Constant Time**

* Execution time does not depend on input size
* Example: Accessing an array by index

```ts
const arr = [10, 20, 30];
console.log(arr[1]); // Always O(1)
```

**O(n) - Linear Time**

* Time grows proportional to input size
* Example: Looping through an array

```ts
arr.forEach(num => console.log(num)); // O(n)
```

**O(log n) - Logarithmic Time**

* Input size gets reduced by half each step
* very efficient for large inputs
* Example: Binary Search (on sorted array)

```ts
function binarySearch(arr: number[], target: number): boolean {
  let left = 0, right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return true;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return false;
}
// O(log n)
```

**O(n²) - Quadratic Time**

* Time grows as the square of the input size
* Typical is nested loops
* Example: Bubble Sort

```ts
function bubbleSort(arr: number[]): number[] {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
}
// O(n²)
```

**Quick Comparison**

| Complexity | Example            | Growth for n=10 | Growth for n=1000 |
| ---------- | ------------------ | --------------- | ----------------- |
| O(1)       | Array index lookup | 1 step          | 1 step            |
| O(n)       | Loop through array | 10 steps        | 1000 steps        |
| O(log n)   | Binary search      | ~3 steps        | ~10 steps         |
| O(n²)     | Bubble sort        | 100 steps       | 1,000,000 steps   |

**Interview Tips**

✅ Be able to explain Big-O  **verbally with examples** .

✅ Common trick: When you see  **nested loops → O(n²)** .

✅ If input size shrinks by half →  **O(log n)** .

✅ For each item processed once →  **O(n)** .

# Arrays

**Definition:** A collection of elements stored in contiguous memory locations (contiguous = back-to-back)

**Structure:** Each element sits right next to the previous one

**Indexing:** You can directly access any element using its index → O(1) - Constant Time

**Resizing:** Fixed size in low-level languages (C,C++). in higher level languages (Python list, JS arrays), resizing is hidden but costly internally

**Pros:**

* Fast Indexing/random access → `O(1)`
* Cache-friendly (CPU likes contiguous memory, faster traversal)

**Cons:**

* Insertion/Deletion in the middle is expensive → `O(n)` (because elements must be shifted)
* Resizing (when full) requires copying to a new bigger block.

**Real-World Analogy**

* **Array = row of lockers** 📚: Each locker is next to the other. You can jump to locker #50 instantly, but if you want to insert a new locker in the middle, you must shift all the others down.

# Linked List

**Definition:**  A collection of nodes where each nodes points to the next node (not stored contiguously in memory)

**Structure:** Each node = data + pointer/reference to the next node

**Traversal:** To access an element, you must start at the head and follow the links → `O(n)`

**Types:**

* Singly linked list (each node points to next)
* Doubly linked list (each node points to next and previous)

**Pros:**

* Dynamic size (no resizing)
* Insertion/Deletion in the middle is cheap → `O(1)` if you already have a pointer to the node

**Cons:**

* No random access → must travers → `O(n)`
* Extra memory for pointers
* Poor cache performace (scattered in memory)

**Real-World Analogy**

* **Linked List = treasure map** 🗺️: Each clue (node) tells you where the next clue is. You can add/remove clues easily, but finding the 50th clue means walking through all the previous ones.

# Hash Maps

A Hash Map stores key, value pairs.

its like a Dictionary

* you look up a key (like `username`)
* And quickly get the value (like `"Bobby"`)

different languages refer to this with a different name :

* Java → HashMap
* Python, C#, Swift → Dictionary
* JavaScript → Map
* C++ → unordered_map

**How it Works**

Hash Function

* the Key is run through a hash function, which converts it into a number ( an index in an array )

Example:

```ts
hash("apple");  → 42
hash("banana"); → 7
```

Store in Array

* That number points to a "bucket" (a slot in an array).
* the value is stored there

Lookup

* when you search for "apple", the same hash function runs, gives 42, and the map looks directly in bucket 42

⚡ **This is why hash maps have average `O(1)` lookup time.**

**Issues That Can Occur:**

**Collisions**

Problem: **Two keys may hash to the same index**

Example:

```ts
hash("apple"); → 42
hash("grape"); → 42
```

* this is called Collision

Solutions to handle Collisions:

1. Chaining (most common)
   * Each bucket stores a list of key-value pairs
   * if `"apple"` and `"grape"` both hash to 42, they both live in bucket 42's list
   * Lookup up checks inside that small list
   * Worst-case performance: `O(n)` if everything collides, but usually still very fast
2. Open Addressing
   * Instead of a list, the map finds the next empty slot in the array
   * More memory-effiecent, but more complex

**Performance**

* Insert: `O(1)` average
* Lookup: `O(1)` average
* Delete: `O(1)` average
* Worst-case: `O(n)` (if collisions go bad, e.g., poor hash functions)

**Real World Example**

* JavaScript's `Map` or plain `{}` objects use hash maps under the hood.
* Eample in Typescript

```ts
const userScores = new Map<string, number>();
userScores.set("Bobby", 95);
userScores.set("Alice", 87);

console.log(userScores.get("Bobby")); // 95

```

✅ **Key Takeaways for Interview**

* Hash maps =  **fast key → value lookups** .
* Use a **hash function** to turn a key into an index.
* Handle **collisions** with **chaining** or  **open addressing** .
* Average `O(1)`, worst-case `O(n)`.

# Recursion

Recursion is when a function calls itself to solve smaller parts of a problem intil it reaches a base case (the stopping condition)

Think of it like looking into 2 mirrors facing each other -- you see infinte reflections, but in code, we stop at the base case to avoid infinite loops

**Structure of Recursion**

Every recursive function has 2 parts:

1. Base Case → when to stop (prevents the infinite loop)
2. Recursive Case → where the function calls itself on smaller input

Example: Factorial `n! - n x (n-1)!`

```ts
function factorial(n:number): number {
     if (n === 0) return 1; // base case
     return n * factorial(n-1); // recursive case
}

console.log(factorial(5)); // outputs 120
```

the way it works is it chains off of itself so the numbers in this factorial example would look like this:

5 * factorial(5-1) → 4 * factorial(4-1) → 3 * factorial(3-1) →  2 * factorial(2-1) → 1 * factorial(1-1) → (base case) n === 0 return 1 so, 1 * 1

all of this results in the output 120

Common Examples:

**Factorial**

*Recursive formula*: `n! - n x (n-1)!` with `0! = 1` as base case

**Fibonacci**

```ts
function fib(n:number): number {
     if (n <= 1) return n;
     return fib(n-1) + fib(n - 2);
}
```

⚠️ This has exponential complexity `O(n²)` → very slow without optimization ( use memoization or iteration instead )

Tree Traversal

This is the perfect example of the Recursive use case

```ts
type Node = {
     value: number,
     left?: Node,
     right?: Node
}

function traverse(node?: Node) {
     if (!node) return; // base Case
     console.log(node.value); // do work
     traverse(node.left); // recursive left
     travers(node.right); // recursive right
}
```

**When to Use Recursion**

When the problem can be broken down into smaller subproblems of the same type

Data structures with a recursive nature:

* Trees (traversals, DFS, backtracing problems)
* Graphs (DFS, connected components)
* Divide and Conquer Algorithms (merge sort, quicksort, binary search)

**Recusuion vs Iteration**

* Recursion is more often elegant, easier to write for problems like tree traversals
* Iteration (loops) is usually more memory-efficient.

🔸Why? Each recursive call adds a new stack frame → uses memory (`O(n)` space for recursion depth). Iterative solutions often need `O(1)` extra space.

Interview Notes

* Always define **base case** clearly (common mistake: forgetting it → infinite recursion).
* Watch for **stack overflow** if recursion depth is too large.
* Interviewers may ask you to **rewrite a recursive solution iteratively** to show you understand tradeoffs.

# Database Indexes

**What is a Database Index?**

A Datbase Index is like the index at the back of the textbook

Instead of flipping through the entire book (table scan), you jump directly tot he right page

* Without Index → the database scans the every row (slow for large tables)
* With Index → The database uses the index (much faster lookups)

**How Indexs Work**

An Index is usually stored as a B-Tree (balanced tree)

Keys are sorted, so searching is `O(log n)` instead of `O(n)`

When you query with `HERE`, the database first checks the index → then fetches the matching row.

Example:

```sql
-- Table without index
SELECT * FROM users WHERE email = 'bob@gmail.com';
-- Scans all rows

-- Add index
CREATE INDEX idx_users_email ON users(email);

-- Now the query jumps straight to 'bob@gmail.com' in log(n) time
```

Types of Indexes

1. **Primary Index** → autmatically created on primary key
2. **Secondary Index** → manually created (e.g. on `email`)
3. **Composite Index** → index on multiple columns `(first_name, last_name)`
4. **Unique Index** → ensures no duplicate values

**Trade-offs (Pros vs Cons)**

**Pros**

* Speed up `SELECT` queries (fast lookups, joins, and sorting)
* Reduce the need for full table scans

**Cons**

* Slower Writes → Every `INSERT`, `UPDATE`, or `DELETE` must also update the index
* Memory Usage → Indexes take up extra disk space
* To Many Indexes → Can slow down performance instead of helping

**🔹 Real-World Example**

Imagine a  **phone book** :

* Without index → You read every name until you find "Larson".
* With index → Names are alphabetized, so you jump straight to "L".

Databases work the same way. Indexes give you a "shortcut."

---

✅  **Key Interview Soundbite** :

*"Indexes improve query speed by reducing lookups from O(n) to O(log n), but they slow down writes since the index itself must be updated. They’re best used on columns frequently queried, but not on every column."*

# Rest APIs

## POST

**Purpose:** Used to create a new resource

**Behavior:**

* The server decides the new resource's ID or URL
* Example : creating a new user, order, or blog post.

**Idempotency:** NOT idempotent → calling it multiple times creates multiple resources

**Analogy:** Like telling a waiter to "*Bring me another coffee.*" → each request create a new coffee

**Example:**

```http
POST /users
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

Response might include:

```http
201 created
Location: /users/123
```

## PUT

**Purpose:** Used to update an existing resource (or create if it does not exist at a specific ID)

**Behavior:**

* The client specifies the resource's ID/URL
* Replaces the entire resource unless it's a partial update (then you'd use PATCH)

**Idempotency:** Idempotent → calling it multiple times results in the same state

**Analogy:** Like saying "*Replace table #3's coffee with a cappuccino*" → it replaces what's there, doesn't add new

**Example:**

```http
PUT /users/123
{
  "name": "Alice",
  "email": "alice.new@example.com"
}
```

Response:

```http
200 OK
```

## GET

**Purpose:** Fetch an existing resource or collection

**Behavior**:

* Does not change the state of the server
* Safe to call multiple times

**Idempotency**: Idempotency → Calling it repeatedly return the same result (unless the resource itself changes externally)

**Analogy:** Like saying: “Waiter, bring me the menu.” → just retrieves info, doesn’t alter anything.

Example:

```http
GET /users/123
```

Response:

```http
200 OK
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

## PATCH

**Purpose:** Update part of an existing resource

**Behavior**:

* Client provide only the fields to update
* Leaves the rest of the resources unchanged

**Idempotency**: Not guarenteed to be idempotent (depends on implementation)

**Analogy:**  Like telling the waiter: “Add sugar to my coffee.” → changes part of the order, not the whole.

Example:

```http
PATCH /users/123
{
  "email": "alice.new@example.com"
}
```

Response:

```http
200 OK
{
  "id": 123,
  "name": "Alice",
  "email": "alice.new@example.com"
}
```

## Delete

**Purpose:** Removes an existing resource

**Behavior**:

* Deletes the resource at the given ID/URL

**Idempotency**: Idempotent → deleting multiple times has the same effect (resource stays deleted)

**Analogy:**  Like saying: “Take away table #3’s coffee.” → once it’s gone, asking again doesn’t change

Example:

```http
DELETE /users/123
```

Response:

```http
204 No Content
```

## HEAD

**Purpose:** Same as GET, but only fetchs headers(metadata)(no body content)

**Behavior**:

* Useful for chacking resource exsitence, size, or last-modified date without downloading full content

**Idempotency**: Idempotent

**Analogy:**

* Like asking: “Does the menu exist, and what’s on the cover?” → you don’t open it fully.

Example:

```http
HEAD /users/123
```

Response

```http
200 OK
Content-Type: application/json
Content-Length: 75
```

## OPTIONS

**Purpose:** Ask the server what HTTP methods are allowed on a resource

**Behavior**:

* Doesnt change anything, just returns allowed methods

**Idempotency**: Idempotent

**Analogy:** Like asking the waiter: “What can I order from this kitchen?” → waiter lists available dishes

Example:

```http
OPTIONS /users/123
```

Response

```http
200 OK
Allow: GET, PUT, PATCH, DELETE, OPTIONS
```



## TRACE

**Purpose:** Echoes back the request so that the client can see whats reaching the server

**Behavior**: 

* The server returns the exact request it recieved (headers, etc)
* used mainly for debugging and testing

**Idempotency**: Idempotent → calling multiple times returns the same result.

**Analogy:** Like asking the waiter: “Repeat my order back to me so I know you heard it correctly.”

Example:

```http
TRACE /users/123
```

Response

```http
200 OK
TRACE /users/123 HTTP/1.1
Host: example.com
User-Agent: curl/7.79.1
```



## CONNECT

**Purpose:** Establish a tunnel to the server, often for encrypted (HTTPS) communication through a proxy**.**

**Behavior**: 

* Tells the server (often a proxy) to open a TCP connection to another host.
* Mostly used in HTTPs requests through proxies

**Idempotency**: Not idempotent (since establishing multiple tunnels changes the state each time).

**Analogy:** Like telling the waiter: “Please connect me to the chef directly so I can speak to them.”

Example:

```http
CONNECT www.example.com:443 HTTP/1.1
Host: www.example.com
```

Response

```http
200 Connection Established
```



# Algorithms

## Sorting Algorithms

---

### Bubble Sort

🔹**What is Bubble Sort?**

Bubble Sort is a  **simple comparison-based sorting algorithm** .

* It works by repeatedly **swapping adjacent elements** if they are in the wrong order.
* After each pass through the list, the largest element "bubbles up" to the end of the list.
* This continues until the array is sorted.



🔹**Step-by-step Explanation**

Let’s say we want to sort this array in ascending order:

```java
[5, 2, 9, 1, 5, 6]
```

**Pass 1:**

* Compare `5` and `2` → swap → `[2, 5, 9, 1, 5, 6]`
* Compare `5` and `9` → no swap
* Compare `9` and `1` → swap → `[2, 5, 1, 9, 5, 6]`
* Compare `9` and `5` → swap → `[2, 5, 1, 5, 9, 6]`
* Compare `9` and `6` → swap → `[2, 5, 1, 5, 6, 9]`

👉 Largest element (`9`) bubbled to the end.

**Pass 2:**

* Compare `2` and `5` → no swap
* Compare `5` and `1` → swap → `[2, 1, 5, 5, 6, 9]`
* Compare `5` and `5` → no swap
* Compare `5` and `6` → no swap

👉 Second largest (`6`) is now in correct place.

Repeat passes until no swaps are needed.

Final result:

```java
[1, 2, 5, 5, 6, 9]
```



🔹**Pseudocode**

```plaintext
procedure bubbleSort(array)
    n = length of array
    repeat
        swapped = false
        for i = 0 to n-2
            if array[i] > array[i+1]
                swap(array[i], array[i+1])
                swapped = true
        end for
    until swapped = false
end procedure
```


🔹**Java Implementation**

```java
public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;

        do {
            swapped = false;
            for (int i = 0; i < n - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    // swap
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    swapped = true;
                }
            }
        } while (swapped);
    }

    public static void main(String[] args) {
        int[] numbers = {5, 2, 9, 1, 5, 6};
        bubbleSort(numbers);
        for (int num : numbers) {
            System.out.print(num + " ");
        }
    }
}

```


🔹TypeScript Implementation

```ts
function bubbleSort(arr: number[]): number[] {
    let n = arr.length;
    let swapped: boolean;

    do {
        swapped = false;
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                // swap
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
                swapped = true;
            }
        }
    } while (swapped);

    return arr;
}

// Example usage
const numbers = [5, 2, 9, 1, 5, 6];
console.log(bubbleSort(numbers)); // [1, 2, 5, 5, 6, 9]
```


🔹**Complexity**

* **Best Case (already sorted):** `O(n)` (because only one pass is needed, with no swaps).
* **Worst Case:** `O(n²)` (when array is in reverse order).
* **Space Complexity:** `O(1)` (in-place sorting, only swaps needed).
* **Stability:** ✅ Stable (equal elements keep their relative order).
