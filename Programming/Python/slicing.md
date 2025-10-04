slicing is one of those things that looks simple but has a ton of tricks that make your code cleaner (and show interviewers you know Python well). Let’s break it down into a  **mini-lesson + practice problems** .

---

## 🔹 Python Slicing Basics

Syntax:

```python
sequence[start:stop:step]
```

* `start` → where to begin (inclusive).
* `end` → where to stop (exclusive).
* `step` → how much to move by (can be negative).

Works on: strings, lists, tuples, basically anything indexable.

---

### ✅ Common Patterns

1. **Reverse a sequence**
   ```python
   nums = [1, 2, 3, 4, 5]
   print(nums[::-1])  # [5, 4, 3, 2, 1]
   ```
2. **Get every other element**
   ```python
   print(nums[::2])   # [1, 3, 5]
   ```
3. **Negative indexes**
   ```python
   text = "hello"
   print(text[-1])   # 'o' (last char)
   print(text[:-1])  # 'hell' (everything but last)
   ```
4. **Slice with custom start/stop**
   ```python
   text = "abcdef"
   print(text[1:5])   # 'bcde'
   print(text[::3])   # 'ad' (every 3rd letter)
   ```

---

## 🔹 Mini Challenges (Your Turn)

Try to write the slicing expressions for these:

1. Given `nums = [10, 20, 30, 40, 50, 60]` → get **[30, 40, 50]**
2. From `"racecar"` → get `"aceca"` (the middle section).
3. From `[1, 2, 3, 4, 5, 6]` → get **[6, 4, 2]** (reverse every other element).
4. From `"python"` → reverse it into `"nohtyp"`.

---



## 🔥 Tricky Slicing Exercises

1. **Skip–Take Pattern**

   From `s = "abcdefghijklmnopqrstuvwxyz"`,

   get `"acegikmoqsuwy"` (every other letter).

---

2. **Chunk Out the Middle**

   From `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]`,

   get `[4, 5, 6]`.

---

3. **Reverse in Chunks**

   From `s = "abcdefghij"`,

   get `"cba fed jih"` (reverse every group of 3).

   (Hint: you’ll need slicing  **inside slicing** .)

---

4. **Mirror Trick**

   From `word = "mirror"`,

   get `"mirrorrim"`.

---

5. **Matrix Diagonal (Bonus 🔥)**

   Given:

   ```python
   mat = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   ```

   Use slicing to get the diagonal `[1, 5, 9]`.

---

💡 The last one is a little sneaky because slicing isn’t always obvious in 2D — but you can pair it with `range` stepping or comprehension.
