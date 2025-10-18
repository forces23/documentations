# 🐍 Python Built-ins

## 1. `any(iterable)`

* Returns `True` if **at least one element** of the iterable is truthy.

```python
nums = [0, 0, 3, 0]
print(any(nums))   # True, because 3 is truthy
```

* Check if **any number is negative**

```python
nums = [5, -3, 8]
print(any(n < 0 for n in nums))   # True
```

* Check if **any string is empty**

```python
words = ["hi", "", "there"]
print(any(len(w) == 0 for w in words))   # True
```


---

## 2. `all(iterable)`

* Returns `True` if **every element** of the iterable is truthy.

```python
nums = [1, 2, 3]
print(all(nums))   # True
nums = [1, 0, 3]
print(all(nums))   # False, because 0 is falsy
```

* Check if **all numbers are even**

```python
nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums))   # True
```

* Check if **all strings are empty**
* ```python
  words = ["", "", ""]
  print(all(len(w) == 0 for w in words))   # True
  ```

## Why any() and all() is Useful

Instead of writing long loops like:

```python
for n in nums:
    if n < 0:
        return True
return False
```

You can do:

```python
return any(n < 0 for n in nums)
```

Much cleaner and faster to read.

---

## 3. `zip(*iterables)`

* Combines multiple iterables element-by-element into tuples.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 70]
print(list(zip(names, scores)))  
# [('Alice', 90), ('Bob', 80), ('Charlie', 70)]
```

---

## 4. `enumerate(iterable, start=0)`

* Gives both **index and value** in a loop.

```python
letters = ["a", "b", "c"]
for i, ch in enumerate(letters, start=1):
    print(i, ch)
# 1 a
# 2 b
# 3 c
```

---

## 5. `sorted(iterable, key=..., reverse=...)`

* Returns a **new sorted list** (doesn’t modify in-place).
* `key=` lets you customize sorting.

```python
letters = ["a", "b", "c"]
for i, ch in enumerate(letters, start=1):
    print(i, ch)
# 1 a
# 2 b
# 3 c
```

---

# 🏋️ Challenges for You

1. Use `any` and `all`:
   * Write a function `all_positive(nums)` that returns `True` if all numbers in a list are > 0.
2. Use `zip`:
   * Given `students = ["Ann", "Ben", "Cara"]` and `grades = [85, 92, 78]`, return a dictionary mapping each student to their grade.
3. Use `enumerate`:
   * Write a function that returns the index of the first negative number in a list (or `-1` if none).
4. Use `sorted` with `key=`:
   * Given `words = ["python", "is", "awesome"]`, return them sorted by length.
