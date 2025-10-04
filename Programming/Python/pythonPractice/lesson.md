
# 📘 Lesson Plan — Python Foundations + Big-O

## **1. Solidify Python Basics**

You’ve shown you know:

* ✅ Lists, dicts, loops, string ops
* ✅ Functions and classes
* ✅ F-strings & ternary usage

But let’s fill a few gaps:

**Practice goals:**

* List comprehensions (not just loops).
* Set operations (union, intersection, difference).
* Dictionary methods (`.get`, `.items`, `.setdefault`).
* Slicing tricks (`[::-1]`, stepping, negative indexes).
* Built-in functions (`any`, `all`, `zip`, `enumerate`, `sorted` with `key=`).

**Mini-Exercises:**

* Given a list of numbers, return a list of their squares (list comprehension).
* Given two sets, find elements unique to each.
* Sort a list of tuples by the second element.
* Reverse a string with slicing.
* Use `enumerate` to loop with both index + value.

---

## **2. Writing Clean Code**

You already write structured code. Let’s push it further.

**Good habits to practice:**

* Use **functions** to break big problems into smaller parts.
* Pick **descriptive variable names** (`nums`, `word_counts`, `is_palindrome`).
* Write a `main()` function and use:

```python
if __name__ == "__main__":
	main()
```

so your code is reusable.

**Mini-Exercises:**

* Refactor your palindrome function so the cleaning logic is its own helper function.
* Refactor your fizzbuzz to return a list instead of printing.

---

## **3. Big-O Complexity (Fill the Gap)**

Right now, you said you’re unsure here — so let’s build intuition.

* **O(1)** → constant time (dict lookup, list append).
* **O(n)** → linear time (loop through a list).
* **O(n²)** → nested loops.
* **O(log n)** → divide-and-conquer (binary search).

**Mini-Exercises:**

* Tell me the Big-O of:
  ```python
  for i in range(n):
      for j in range(n):
          print(i, j)
  ```
* What about:
  ```python
  if x in my_dict:
      print(my_dict[x])
  ```
* What about:
  ```python
  nums = [1,2,3,4,5]
  print(nums[::-1])
  ```

---

## **4. Apply Knowledge to Easy Problems (10–15 reps)**

Before tackling medium LeetCode, build fluency:

* Remove duplicates from a list (using sets).
* Find the maximum in a list (loop or `max`).
* Reverse a string.
* Check if two strings are anagrams.
* Find the most frequent element in a list.
* Merge two sorted lists.
* Implement binary search.

---

# ✅ Next Steps

Here’s what I’d suggest:

1. Work through the **mini-exercises** above so I can check your gaps.
2. We’ll then move into **Big-O reasoning + easy problems** until you’re fluent.
3. After that, you’ll be ready for structured LeetCode study.
