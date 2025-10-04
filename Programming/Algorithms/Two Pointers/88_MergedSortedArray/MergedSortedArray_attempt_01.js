/**
 * LeetCode #88: Merge Sorted Array
 * 
 * Problem Description:
 * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
 * representing the number of elements in nums1 and nums2 respectively.
 * 
 * Merge nums1 and nums2 into a single array sorted in non-decreasing order.
 * 
 * The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
 * To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
 * and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 * 
 * Example 1:
 * Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
 * Output: [1,2,2,3,5,6]
 * Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
 * The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
 * 
 * Example 2:
 * Input: nums1 = [1], m = 1, nums2 = [], n = 0
 * Output: [1]
 * Explanation: The arrays we are merging are [1] and [].
 * The result of the merge is [1].
 * 
 * Example 3:
 * Input: nums1 = [0], m = 0, nums2 = [1], n = 1
 * Output: [1]
 * Explanation: The arrays we are merging are [] and [1].
 * The result of the merge is [1].
 * Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 * 
 * Constraints:
 * - nums1.length == m + n
 * - nums2.length == n
 * - 0 <= m, n <= 200
 * - 1 <= m + n <= 200
 * - -10^9 <= nums1[i], nums2[j] <= 10^9
 * 
 * Follow up: Can you come up with an algorithm that runs in O(m + n) time?
 */

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1, m, nums2, n) {
    // TODO: Implement the merge function
    // Hint: Consider working from the end of the arrays to avoid overwriting elements
    console.log(`m: ${m}`);
    console.log(`n: ${n}`);

    // if (m === 0) nums1 = [...nums2];

    let largestNumPos = m + n - 1; // will tell where the largest number will go starting from the end
    let p1 = m - 1; // postion in nums1 starting from the end
    let p2 = n - 1; // postion in numss starting at the end

    console.log(`nums1[p1]: ${nums1[p1]}`);
    console.log(`nums2[p2]: ${nums2[p2]}`);

    while (p1 >= 0 && p2 >= 0) {
        // nums1[p1] is greater than nums2[p2] set nums1[largestNumPos] to nums1[p1], decrement p1 and largestNumPos
        if (nums1[p1] > nums2[p2]) {
            nums1[largestNumPos] = nums1[p1];
            p1--;
        } else {
            nums1[largestNumPos] = nums2[p2];
            p2--;
        }
        largestNumPos--;
    }

    // add the remiaing the numbers from nums2 into nums1
    while (p2 >= 0) {
        nums1[largestNumPos] = nums2[p2];
        p2--;
        largestNumPos--;
    }
}

// Test cases
function runTestCase(nums1, m, nums2, n, expected) {
    const originalNums1 = [...nums1];
    merge(nums1, m, nums2, n);
    console.log(`Input: nums1 = [${originalNums1}], m = ${m}, nums2 = [${nums2}], n = ${n}`);
    console.log(`Output: [${nums1}]`);
    console.log(`Expected: [${expected}]`);
    console.log(`Result: ${arraysEqual(nums1, expected) ? 'PASS ✓' : 'FAIL ✗'}`);
    console.log('---');
}

// Helper function to check if arrays are equal
function arraysEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) return false;
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }
    return true;
}

// Run test cases
console.log('LeetCode #88: Merge Sorted Array - Test Cases');
console.log('===========================================');
runTestCase([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]);
runTestCase([1], 1, [], 0, [1]);
runTestCase([0], 0, [1], 1, [1]);
runTestCase([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]);
runTestCase([1, 2, 3, 0, 0, 0, 0], 3, [2, 5, 6, 7], 4, [1, 2, 2, 3, 5, 6, 7]);