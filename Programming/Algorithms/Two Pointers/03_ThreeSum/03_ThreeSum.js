/**
 * Challenge 3: Three Sum
 * 
 * Problem Description:
 * Given an integer array 'nums', return all the triplets [nums[i], nums[j], nums[k]] 
 * such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * 
 * Notice that the solution set must not contain duplicate triplets.
 * 
 * Example 1:
 * Input: nums = [-1, 0, 1, 2, -1, -4]
 * Output: [[-1, -1, 2], [-1, 0, 1]]
 * 
 * Example 2:
 * Input: nums = []
 * Output: []
 * 
 * Example 3:
 * Input: nums = [0]
 * Output: []
 * 
 * Constraints:
 * - 0 <= nums.length <= 3000
 * - -10^5 <= nums[i] <= 10^5
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
function threeSum(nums) {
    // TODO: Implement the two pointers solution
    // Hint: Sort the array first, then use one fixed pointer and two moving pointers

    // if array is less then 3 then return empty array
    if (nums.length < 3) return [];

    nums.sort((a, b) => a - b); //Sort the array in ascending order

    const result = [];

    // Iterate throught the array, fixing one element at a time 
    // we stop at the length -2 because we need at least 2 more elements to for the pair
    for (let i = 0; i < nums.length - 2; i++) {
        // Skip dups for the fixed element
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        // set up the 2 pointers here
        let left = i + 1;               // start right after the fixed element 
        let right = nums.length - 1;   // end of the array

        //Target sum is the negative og the fixed element
        const target = -nums[i];

        while (left < right) {
            const sum = nums[left] + nums[right];

            if (sum === target) {
                // Found a triplet
                result.push([nums[i], nums[left], nums[right]]);

                //skip dups for the left and right pointers
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (right > left && nums[right] === nums[right - 1]) right--;

                // Move both pointers
                left++;
                right++;

                // if no triplet was found then continue with handling the duplicates and moving pointers
            } else if (sum < target) {
                //Sum is too small, move left pointer to increase the sum
                left++;
            } else {
                //Sum is too large, move right pointer to decrease the sum
                right--;
            }

        }

    }

    return result; // Return array of triplets
}

// Test cases
console.log(threeSum([-1, 0, 1, 2, -1, -4])); // Expected: [[-1, -1, 2], [-1, 0, 1]]
console.log(threeSum([]));                    // Expected: []
console.log(threeSum([0]));                   // Expected: []