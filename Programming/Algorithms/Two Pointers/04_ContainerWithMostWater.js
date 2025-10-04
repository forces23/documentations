/**
 * Challenge 4: Container With Most Water
 * 
 * Problem Description:
 * Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 * n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
 * Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
 * 
 * Notice that you may not slant the container.
 * 
 * Example 1:
 * Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
 * Output: 49
 * Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
 * In this case, the max area of water (blue section) the container can contain is 49.
 * 
 * Example 2:
 * Input: height = [1, 1]
 * Output: 1
 * 
 * Example 3:
 * Input: height = [4, 3, 2, 1, 4]
 * Output: 16
 * 
 * Example 4:
 * Input: height = [1, 2, 1]
 * Output: 2
 * 
 * Constraints:
 * - n == height.length
 * - 2 <= n <= 10^5
 * - 0 <= height[i] <= 10^4
 */

/**
 * @param {number[]} height
 * @return {number}
 */
function maxArea(height) {
    // TODO: Implement the two pointers solution
    // Hint: Use two pointers at the beginning and end of the array
    
    return 0; // Return the maximum area
}

// Test cases
console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])); // Expected: 49
console.log(maxArea([1, 1]));                      // Expected: 1
console.log(maxArea([4, 3, 2, 1, 4]));             // Expected: 16
console.log(maxArea([1, 2, 1]));                   // Expected: 2