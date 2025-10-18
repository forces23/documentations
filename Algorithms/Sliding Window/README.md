# Sliding Window Algorithm Pattern

This folder contains resources for learning and practicing the Sliding Window algorithm pattern.

## What is the Sliding Window Technique?

The Sliding Window technique is an algorithmic pattern that aims to reduce the use of nested loops and replace them with a single loop, thereby reducing the time complexity.

This technique shows how a nested loop in some problems can be converted to a single loop to reduce the time complexity from O(n²) or O(n³) to O(n).

## How It Works

1. Create a window of certain size (can be fixed or variable)
2. Slide the window across the data (typically an array or string)
3. Process the data within the current window
4. Update the window by adding elements from one end and removing from the other

## Types of Sliding Window

### Fixed Size Window
- The window size remains constant throughout the algorithm
- Example: Find the maximum sum of any contiguous subarray of size k

```javascript
function maxSumSubarrayOfSizeK(arr, k) {
    let maxSum = 0;
    let windowSum = 0;
    let windowStart = 0;
    
    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        windowSum += arr[windowEnd]; // Add the next element
        
        // Slide the window once we hit size k
        if (windowEnd >= k - 1) {
            maxSum = Math.max(maxSum, windowSum);
            windowSum -= arr[windowStart]; // Remove the element going out
            windowStart++; // Slide the window ahead
        }
    }
    
    return maxSum;
}
```

### Variable Size Window
- The window size changes based on certain conditions
- Example: Find the smallest subarray with a sum greater than or equal to a given value

```javascript
function smallestSubarrayWithGivenSum(arr, targetSum) {
    let minLength = Infinity;
    let windowSum = 0;
    let windowStart = 0;
    
    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        windowSum += arr[windowEnd]; // Add the next element
        
        // Shrink the window as small as possible while maintaining the sum >= targetSum
        while (windowSum >= targetSum) {
            minLength = Math.min(minLength, windowEnd - windowStart + 1);
            windowSum -= arr[windowStart]; // Remove the element going out
            windowStart++; // Shrink the window
        }
    }
    
    return minLength === Infinity ? 0 : minLength;
}
```

## When to Use Sliding Window

The Sliding Window pattern is useful when:

1. You need to process contiguous subarrays or substrings
2. You're looking for a min, max, longest, shortest, or a specific condition in a contiguous sequence
3. The problem involves calculating something among all subarrays of a given size

## Common Applications

- Maximum/minimum sum subarray of size k
- Longest substring with k distinct characters
- String anagrams or permutations
- Maximum number of fruits in baskets (distinct elements in a subarray)
- Longest substring without repeating characters

## Resources in this Folder

- **LeetCodeProblems.md**: A list of LeetCode problems categorized by difficulty that can be solved using the Sliding Window technique

## Practice Tips

1. Start with fixed-size window problems as they're typically easier
2. Move on to variable-size window problems once you're comfortable
3. Pay attention to how the window expands and contracts
4. Be careful with edge cases (empty arrays, single elements, etc.)
5. Practice tracking multiple variables within the window

Happy coding!