# Sliding Window LeetCode Problems

This file contains 30 LeetCode problems (10 easy, 10 medium, 10 hard) that can be solved using the Sliding Window technique. Each problem includes its difficulty level, problem number, and link to the LeetCode page.

## Easy Problems

1. **Maximum Average Subarray I** (Problem #643)
   - https://leetcode.com/problems/maximum-average-subarray-i/
   - Find the contiguous subarray of given length k that has the maximum average value.

2. **Minimum Size Subarray Sum** (Problem #209)
   - https://leetcode.com/problems/minimum-size-subarray-sum/
   - Find the minimal length of a contiguous subarray with a sum ≥ target.

3. **Longest Continuous Increasing Subsequence** (Problem #674)
   - https://leetcode.com/problems/longest-continuous-increasing-subsequence/
   - Find the length of the longest continuous increasing subsequence.

4. **Subarray Product Less Than K** (Problem #713)
   - https://leetcode.com/problems/subarray-product-less-than-k/
   - Count subarrays where the product of all elements is less than k.

5. **Longest Substring with At Most Two Distinct Characters** (Problem #159)
   - https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
   - Find the longest substring that contains at most 2 distinct characters.

6. **Grumpy Bookstore Owner** (Problem #1052)
   - https://leetcode.com/problems/grumpy-bookstore-owner/
   - Find the maximum number of customers that can be satisfied.

7. **Diet Plan Performance** (Problem #1176)
   - https://leetcode.com/problems/diet-plan-performance/
   - Calculate the diet performance based on a sliding window of calories.

8. **Find K-Length Substrings With No Repeated Characters** (Problem #1100)
   - https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
   - Count the number of substrings of length K with no repeated characters.

9. **Defuse the Bomb** (Problem #1652)
   - https://leetcode.com/problems/defuse-the-bomb/
   - Replace each element with the sum of the next k elements.

10. **Contains Duplicate II** (Problem #219)
    - https://leetcode.com/problems/contains-duplicate-ii/
    - Find if there are duplicates within distance k.

## Medium Problems

1. **Longest Substring Without Repeating Characters** (Problem #3)
   - https://leetcode.com/problems/longest-substring-without-repeating-characters/
   - Find the length of the longest substring without repeating characters.

2. **Longest Repeating Character Replacement** (Problem #424)
   - https://leetcode.com/problems/longest-repeating-character-replacement/
   - Find the longest substring with the same letter after replacement.

3. **Permutation in String** (Problem #567)
   - https://leetcode.com/problems/permutation-in-string/
   - Check if one string's permutation is the substring of another string.

4. **Find All Anagrams in a String** (Problem #438)
   - https://leetcode.com/problems/find-all-anagrams-in-a-string/
   - Find all start indices of anagrams of a pattern in a string.

5. **Fruit Into Baskets** (Problem #904)
   - https://leetcode.com/problems/fruit-into-baskets/
   - Find the longest subarray with at most two distinct elements.

6. **Max Consecutive Ones III** (Problem #1004)
   - https://leetcode.com/problems/max-consecutive-ones-iii/
   - Find the longest subarray with at most K zeros.

7. **Subarrays with K Different Integers** (Problem #992)
   - https://leetcode.com/problems/subarrays-with-k-different-integers/
   - Count the number of subarrays with exactly K different integers.

8. **Longest Substring with At Most K Distinct Characters** (Problem #340)
   - https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
   - Find the longest substring that contains at most k distinct characters.

9. **Count Number of Nice Subarrays** (Problem #1248)
   - https://leetcode.com/problems/count-number-of-nice-subarrays/
   - Count the number of subarrays with exactly k odd numbers.

10. **Maximum Points You Can Obtain from Cards** (Problem #1423)
    - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
    - Maximize points by taking cards from either end of the row.

## Hard Problems

1. **Minimum Window Substring** (Problem #76)
   - https://leetcode.com/problems/minimum-window-substring/
   - Find the minimum window in a string that contains all characters of another string.

2. **Sliding Window Maximum** (Problem #239)
   - https://leetcode.com/problems/sliding-window-maximum/
   - Find the maximum element in each sliding window of size k.

3. **Substring with Concatenation of All Words** (Problem #30)
   - https://leetcode.com/problems/substring-with-concatenation-of-all-words/
   - Find all starting indices of substring(s) that is a concatenation of each word exactly once.

4. **Longest Substring with At Most K Distinct Characters** (Problem #340)
   - https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
   - Find the longest substring that contains at most k distinct characters.

5. **Minimum Number of K Consecutive Bit Flips** (Problem #995)
   - https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
   - Find the minimum number of k-bit flips to make all bits 1.

6. **Count Subarrays with Fixed Bounds** (Problem #2444)
   - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
   - Count subarrays where min is minK and max is maxK.

7. **Maximum Number of Robots Within Budget** (Problem #2398)
   - https://leetcode.com/problems/maximum-number-of-robots-within-budget/
   - Find the maximum number of consecutive robots within budget.

8. **Shortest Subarray with Sum at Least K** (Problem #862)
   - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
   - Find the length of the shortest subarray with sum at least K.

9. **Subarrays with K Different Integers** (Problem #992)
   - https://leetcode.com/problems/subarrays-with-k-different-integers/
   - Count the number of subarrays with exactly K different integers.

10. **Constrained Subsequence Sum** (Problem #1425)
    - https://leetcode.com/problems/constrained-subsequence-sum/
    - Find the maximum sum of a subsequence with constraints.

## Tips for Sliding Window Problems

1. **Identify the window**: Determine what constitutes your "window" - is it a fixed size or variable?

2. **Window expansion and contraction**:
   - For fixed-size windows: Slide the window one element at a time
   - For variable-size windows: Expand until a condition is violated, then contract until it's satisfied again

3. **Track window state**: Keep track of relevant information about the current window (sum, count of elements, etc.)

4. **Optimize calculations**: When sliding the window, update the state incrementally rather than recalculating

5. **Common patterns**:
   - Fixed window size: Often used for averages, sums of fixed length
   - Variable window size: Often used for "longest/shortest subarray that satisfies condition X"
   - Window with constraints: Track additional state to ensure constraints are met

6. **Data structures**: Consider using:
   - HashMap/Counter for frequency of elements
   - Deque for maintaining ordered elements (especially for sliding window maximum/minimum)
   - Set for tracking distinct elements

Happy coding!