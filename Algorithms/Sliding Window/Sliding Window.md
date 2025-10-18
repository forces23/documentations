# **Sliding Window Technique**

The **sliding window** technique is a powerful algorithmic pattern used to efficiently solve problems involving **arrays, strings, or sequences** where you need to track a **contiguous subarray or substring** that meets certain conditions.

---

## **1. What is the Sliding Window Technique?**

* **Definition** : A "window" (a range of indices) slides over the data structure to maintain a subset of elements that satisfy a given condition.
* **Goal** : Optimize brute-force solutions from **O(n²) → O(n)** by avoiding nested loops.
* **Key Features** :
* Uses **two pointers** (`left` and `right`) to represent the window bounds.
* Dynamically **expands** or **shrinks** the window based on conditions.
* Tracks **aggregates** (e.g., sum, max/min length, character counts).

---

## **2. When to Use Sliding Window?**

### **Problem Patterns Where Sliding Window Works Best**

1. **Subarray/Substring Problems**
   * *Example* : Find the longest substring without repeating characters.
   * *Why?* The window maintains a valid segment of the string.
2. **Fixed or Variable-Size Window**
   * *Fixed* : Find the max average of `k` consecutive elements.
   * *Variable* : Smallest subarray with sum ≥ `k`.
3. **Optimization Problems**
   * *Example* : Minimum window substring containing all characters of a pattern.
   * *Why?* The window adjusts to find the optimal solution.
4. **Frequency/Condition Tracking**
   * *Example* : Longest subarray with at most two distinct elements.
   * *Why?* A hash map can track frequencies within the window.

---

## **3. How to Spot Sliding Window Problems in Coding Assessments**

### **Clues in Problem Statements**

* Keywords:
  * "Subarray," "substring," or "contiguous sequence."
  * "Longest," "shortest," "minimum," or "maximum."
  * "Sum," "average," or "frequency."

### **Example Problems**

1. **Fixed-Size Window**
   * *Problem* : Given an array, find the max sum of any `k` consecutive elements.
   * *LeetCode* : [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/).
2. **Variable-Size Window**
   * *Problem* : Find the smallest subarray with sum ≥ `k`.
   * *LeetCode* : [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/).
3. **Frequency-Based Window**
   * *Problem* : Longest substring with at most `k` distinct characters.
   * *LeetCode* : [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/).
4. **Optimization with Constraints**
   * *Problem* : Minimum window in `s` containing all characters of `t`.
   * *LeetCode* : [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/).

---

## **4. Sliding Window Approaches**

### **A. Fixed-Size Window**

* The window size (`k`) is constant.
* Compute a value (e.g., sum) for the first window, then slide it forward while updating the result.

#### **Example: Max Sum of `k` Consecutive Elements**

```javascript
function maxSumSubarray(nums, k) {
  let maxSum = 0, windowSum = 0;
  
  // Compute the first window
  for (let i = 0; i < k; i++) {
    windowSum += nums[i];
  }
  maxSum = windowSum;

  // Slide the window forward
  for (let i = k; i < nums.length; i++) {
    windowSum = windowSum - nums[i - k] + nums[i]; // Remove leftmost, add new right
    maxSum = Math.max(maxSum, windowSum);
  }
  
  return maxSum;
}
```

 **Time Complexity** : O(n)
 **Space Complexity** : O(1)

---

### **B. Variable-Size Window**

* The window size changes dynamically based on a condition.
* Expand the window (`right++`) when the condition is met, shrink it (`left++`) when it’s violated.

#### **Example: Smallest Subarray with Sum ≥ `k`**

```javascript
function minSubArrayLen(nums, k) {
  let left = 0, sum = 0, minLen = Infinity;

  for (let right = 0; right < nums.length; right++) {
    sum += nums[right];
  
    // Shrink the window while sum >= k
    while (sum >= k) {
      minLen = Math.min(minLen, right - left + 1);
      sum -= nums[left];
      left++;
    }
  }
  
  return minLen === Infinity ? 0 : minLen;
}
```

 **Time Complexity** : O(n)
 **Space Complexity** : O(1)

---

### **C. Frequency-Based Window (Hash Map + Sliding Window)**

* Tracks character/word frequencies within the window.
* Expands/shrinks based on frequency constraints.

#### **Example: Longest Substring Without Repeating Characters**

```javascript
function lengthOfLongestSubstring(s) {
  let left = 0, maxLen = 0;
  const charMap = new Map(); // Tracks last index of each character

  for (let right = 0; right < s.length; right++) {
    if (charMap.has(s[right])) {
      left = Math.max(left, charMap.get(s[right]) + 1); // Move left past the duplicate
    }
    charMap.set(s[right], right);
    maxLen = Math.max(maxLen, right - left + 1);
  }
  
  return maxLen;
}
```

 **Time Complexity** : O(n)
 **Space Complexity** : O(min(m, n)) (where `m` is the character set size)

---

## **5. Time & Space Complexity**

| Technique            | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Fixed-Size Window    | O(n)            | O(1)             |
| Variable-Size Window | O(n)            | O(1)             |
| Frequency-Based      | O(n)            | O(k) (hash map)  |

---

## **6. Key Takeaways**

✅ **Use sliding window when:**

* The problem involves  **contiguous subarrays/substrings** .
* You need to optimize  **O(n²) brute-force solutions** .
* The solution requires tracking  **aggregates (sum, frequency, etc.)** .

✅ **Fixed-size window** → Constant `k`.
✅ **Variable-size window** → Dynamic bounds.
✅ **Frequency-based window** → Use a hash map for tracking.


## **7. Practice Problems**

### **Easy**

* [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
* [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

### **Medium**

* [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

### **Hard**

* [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
* [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
