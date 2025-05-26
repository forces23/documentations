### **Two-Pointer Algorithm Technique**

The **two-pointer technique** is a powerful strategy for solving array and linked list problems efficiently. It involves using two pointers (indices or references) to traverse the data structure in a way that reduces time complexity, often from  **O(n²) to O(n)** .

---

## **1. What is the Two-Pointer Technique?**

* **Definition** : Two pointers traverse the array/list in a coordinated manner (e.g., one slow, one fast, or one from the start and one from the end).
* **Goal** : Solve problems with optimal time ( **O(n)** ) and space ( **O(1)** ) complexity.
* **Key Use Cases** :
* Removing duplicates in a sorted array.
* Finding pairs that sum to a target.
* Reversing an array or linked list.
* Detecting cycles in a linked list (Floyd’s algorithm).

---

## **2. When to Use Two-Pointers?**

### **Problem Patterns Where Two-Pointers Shine**

1. **Sorted Arrays/Lists**
   * Example: Remove duplicates, merge two sorted arrays, or find a pair with a target sum.
   * Why? Sorting ensures predictable element arrangement.
2. **Sliding Window Problems**
   * Example: Find the longest subarray with a sum ≤ `k`.
   * Why? Two pointers define a dynamic window.
3. **In-Place Modifications**
   * Example: Move all zeros to the end of an array.
   * Why? Avoid extra space by overwriting elements.
4. **Linked List Traversal**
   * Example: Detect cycles, find the middle node, or reverse a list.
   * Why? Fast and slow pointers efficiently traverse nodes.

---

## **3. How to Spot Two-Pointer Problems in Coding Assessments**

### **Clues in Problem Statements**

* Keywords:
  * "Sorted array"
  * "In-place modification"
  * "Return the indices/values of two elements"
  * "O(1) space" or "O(n) time" constraints.

### **Example Problems**

1. **Remove Duplicates from Sorted Array**
   * Input: `[0,0,1,1,1,2,2,3,3,4]`
   * Output: `[0,1,2,3,4,_,_,_,_,_]` (first `k` elements unique).
2. **Two Sum (Sorted Input)**
   * Input: `[2,7,11,15]`, target = `9`
   * Output: `[0,1]` (indices where `2 + 7 = 9`).
3. **Move Zeroes to End**
   * Input: `[0,1,0,3,12]`
   * Output: `[1,3,12,0,0]`.
4. **Linked List Cycle Detection**
   * Input: A linked list with a cycle.
   * Output: `true` if a cycle exists.

---

## **4. Types of Two-Pointer Approaches**

### **A. Opposite Direction (Converging Pointers)**

* **Use Case** : Searching for pairs (e.g., two sum, palindrome checks).
* **How It Works** :
* One pointer starts at the  **beginning** , the other at the  **end** .
* Move pointers toward each other based on comparisons.

#### **Example: Two Sum in Sorted Array**

```javascript
// JavaScript Example

function twoSum(nums, target) {
    let left = 0, right = nums.length - 1;
    while (left < right) {
        const sum = nums[left] + nums[right];
        if (sum === target) return [left, right];
        else if (sum < target) left++;
        else right--;
    }
    return [];
}
```

### **B. Same Direction (Slow-Fast Pointers)**

* **Use Case** : Removing duplicates, sliding window, or cycle detection.
* **How It Works** :
* `slow` pointer tracks the position for the next valid element.
* `fast` pointer scans ahead to find new valid elements.

#### **Example: Remove Duplicates**

```javascript
// JavaScript Example

function removeDuplicates(nums) {
    let slow = 0;
    for (let fast = 1; fast < nums.length; fast++) {
        if (nums[fast] !== nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }
    return slow + 1;
}
```

### **C. Fast-Slow in Linked Lists (Floyd’s Algorithm)**

* **Use Case** : Detect cycles or find the middle node.
* **How It Works** :
* `slow` moves 1 step at a time.
* `fast` moves 2 steps.
* If they meet, a cycle exists.

#### **Example: Linked List Cycle Detection**

```javascript
// JavaScript Example

function hasCycle(head) {
    let slow = head, fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow === fast) return true;
    }
    return false;
}
```

---

## **5. Time & Space Complexity**

| Technique            | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Opposite Direction   | O(n)            | O(1)             |
| Same Direction       | O(n)            | O(1)             |
| Fast-Slow (Floyd’s) | O(n)            | O(1)             |


## Practice Problems to Master Two-Pointers

1. **Easy**
   * [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
   * [Two Sum II (Sorted Input)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
   * [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
2. **Medium**
   * [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
   * [3Sum](https://leetcode.com/problems/3sum/)
   * [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
3. **Hard**
   * [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
   * [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
