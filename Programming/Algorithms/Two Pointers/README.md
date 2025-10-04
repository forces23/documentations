# Two Pointers Algorithm Practice

This folder contains 5 LeetCode-style coding challenges that focus on the Two Pointers technique. These challenges are designed to help you practice and master this important algorithm pattern.

## What is the Two Pointers Technique?

The Two Pointers technique is an approach where two pointers iterate through a data structure (usually an array) to solve a problem efficiently. The pointers can move toward each other, away from each other, or at different speeds.

## Generic Example: Palindrome Check

Here's a simple example of using the Two Pointers technique to check if a string is a palindrome:

```javascript
function isPalindrome(s) {
    // Convert to lowercase and remove non-alphanumeric characters
    s = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    
    // Use two pointers: one from start, one from end
    let left = 0;
    let right = s.length - 1;
    
    while (left < right) {
        // If characters don't match, it's not a palindrome
        if (s[left] !== s[right]) {
            return false;
        }
        
        // Move pointers toward each other
        left++;
        right--;
    }
    
    // If we get here, it's a palindrome
    return true;
}

// Examples
console.log(isPalindrome("A man, a plan, a canal: Panama"));  // true
console.log(isPalindrome("race a car"));                      // false
```

This example demonstrates how two pointers moving toward each other can efficiently solve a problem with O(n) time complexity and O(1) space complexity (excluding the string processing).

## Challenges Included

1. **Two Sum - Sorted Array**: Find two numbers in a sorted array that add up to a specific target.
   - Difficulty: Easy
   - File: `01_TwoSum.js`

2. **Remove Duplicates from Sorted Array**: Remove duplicates from a sorted array in-place.
   - Difficulty: Easy
   - File: `02_RemoveDuplicates.js`

3. **Three Sum**: Find all unique triplets in the array that sum to zero.
   - Difficulty: Medium
   - File: `03_ThreeSum.js`

4. **Container With Most Water**: Find two lines that together with the x-axis form a container that holds the most water.
   - Difficulty: Medium
   - File: `04_ContainerWithMostWater.js`

5. **Trapping Rain Water**: Calculate how much water can be trapped after raining.
   - Difficulty: Hard
   - File: `05_TrappingRainWater.js`

## How to Use These Challenges

1. Each file contains:
   - A detailed problem description
   - Examples with expected outputs
   - Constraints
   - A function signature for you to implement
   - Test cases to verify your solution

2. Try to solve each problem on your own.

3. Run your JavaScript code using Node.js:
   ```
   node 01_TwoSum.js
   ```

## Tips for Two Pointers Problems

- For sorted arrays, consider using pointers at opposite ends
- For problems involving pairs or triplets, sorting first often helps
- When dealing with subarrays or subsequences, try using fast and slow pointers
- Pay attention to duplicate elements if the problem requires unique results

Happy coding!