/**
 * Challenge 2: Remove Duplicates from Sorted Array
 * 
 * Problem Description:
 * Given a sorted array 'nums', remove the duplicates in-place such that each element appears only once
 * and returns the new length.
 * 
 * Do not allocate extra space for another array. You must do this by modifying the input array in-place
 * with O(1) extra memory.
 * 
 * Clarification:
 * Confused why the returned value is an integer but your answer is an array?
 * Note that the input array is passed by reference, which means a modification to the input array
 * will be known to the caller as well.
 * 
 * Example 1:
 * Input: nums = [1, 1, 2]
 * Output: 2, nums = [1, 2, _]
 * Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2.
 * It doesn't matter what you leave beyond the returned length.
 * 
 * Example 2:
 * Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
 * Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
 * Explanation: Your function should return length = 5, with the first five elements being 0, 1, 2, 3, and 4.
 * It doesn't matter what you leave beyond the returned length.
 * 
 * Constraints:
 * - 0 <= nums.length <= 3 * 10^4
 * - -10^4 <= nums[i] <= 10^4
 * - nums is sorted in ascending order
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
function removeDuplicates(nums) {
    // TODO: Implement the two pointers solution
    // Hint: Use one pointer for iteration and one for placement of unique elements
    
    return 0; // Return the new length
}

// Test cases
const test1 = [1, 1, 2];
console.log(removeDuplicates(test1)); // Expected output: 2
console.log(test1.slice(0, 2));       // Expected: [1, 2]

const test2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
console.log(removeDuplicates(test2)); // Expected output: 5
console.log(test2.slice(0, 5));       // Expected: [0, 1, 2, 3, 4]

const test3 = [0, 0, 1, 2, 2, 3, 4, 5, 5];
console.log(removeDuplicates(test3)); // Expected output: 6
console.log(test3.slice(0, 6));       // Expected: [0, 1, 2, 3, 4, 5]