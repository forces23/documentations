/**
 * Challenge 5: Trapping Rain Water
 * 
 * Problem Description:
 * Given n non-negative integers representing an elevation map where the width of each bar is 1,
 * compute how much water it can trap after raining.
 * 
 * Example 1:
 * Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
 * Output: 6
 * Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 * In this case, 6 units of rain water are being trapped.
 * 
 * Example 2:
 * Input: height = [4, 2, 0, 3, 2, 5]
 * Output: 9
 * 
 * Constraints:
 * - n == height.length
 * - 0 <= n <= 3 * 10^4
 * - 0 <= height[i] <= 10^5
 */

/**
 * @param {number[]} height
 * @return {number}
 */
function trap(height) {
    // TODO: Implement the two pointers solution
    // Hint: Use two pointers and track the maximum height from both left and right
    
    return 0; // Return the total amount of trapped water
}

// Test cases
console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])); // Expected: 6
console.log(trap([4, 2, 0, 3, 2, 5]));                   // Expected: 9