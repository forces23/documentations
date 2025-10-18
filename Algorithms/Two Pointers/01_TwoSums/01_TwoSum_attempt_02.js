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
    // This solution is the most optimized version it takes advantage of the sorted array

    let left = 0;
    let right = numbers.length - 1

    while (left < right) {
        const sum = numbers[left] + numbers[right];

        if (sum === target ){ // if target is met then return the array if the indexs
            return [left + 1, right + 1];
        } else if (sum < target ) { // if sum is less then target then you can go higher on the left side since the array is sorted it will increment smaller numbers first this way
            left++;
        } else { // if the sum is actually larger then the target then the right most number is too large and needs to move to move a step down which would be a smaller number
            right--;
        }
    }
    // if it makes it here then there was no pair that added up to make the target
    return []; // Return the indices of the two numbers
}

// Test cases
console.log(twoSum([2, 7, 11, 15], 9)); // Expected output: [1, 2]
console.log(twoSum([2, 3, 4], 6));      // Expected output: [1, 3]
console.log(twoSum([-1, 0], -1));       // Expected output: [1, 2]

//Edge cases
console.log(twoSum([2, 7, 11, 15], 100)); // Expected output: []
console.log(twoSum([2, 7, 11, 15], 26)); // Expected output: [3, 4]