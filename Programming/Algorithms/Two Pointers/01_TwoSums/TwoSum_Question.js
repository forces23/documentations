/**
 * Challenge 1: Two Sum - Sorted Array
 * 
 * Problem Description:
 * Given a 1-indexed array of integers 'numbers' that is already sorted in non-decreasing order,
 * find two numbers such that they add up to a specific 'target' number.
 * Return the indices of the two numbers as an array [index1, index2] where index1 < index2.
 * 
 * You may assume that each input would have exactly one solution and you cannot use the same element twice.
 * 
 * Example 1:
 * Input: numbers = [2, 7, 11, 15], target = 9
 * Output: [1, 2]
 * Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.
 * 
 * Example 2:
 * Input: numbers = [2, 3, 4], target = 6
 * Output: [1, 3]
 * 
 * Example 3:
 * Input: numbers = [-1, 0], target = -1
 * Output: [1, 2]
 * 
 * Constraints:
 * - 2 <= numbers.length <= 3 * 10^4
 * - -1000 <= numbers[i] <= 1000
 * - numbers is sorted in non-decreasing order
 * - -1000 <= target <= 1000
 * - The tests are generated such that there is exactly one solution
 * 
 * Follow-up: Can you solve it using only O(1) extra space?
 */

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
function twoSum(numbers, target) {
    // TODO: Implement the two pointers solution
    // Hint: Use two pointers, one starting from the beginning and one from the end

    return []; // Return the indices of the two numbers
}

// Test cases
console.log(twoSum([2, 7, 11, 15], 9)); // Expected output: [1, 2]
console.log(twoSum([2, 3, 4], 6));      // Expected output: [1, 3]
console.log(twoSum([-1, 0], -1));       // Expected output: [1, 2]
