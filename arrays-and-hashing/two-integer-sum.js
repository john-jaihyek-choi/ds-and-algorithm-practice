class Solution {
  /**
   * @param {number[]} nums
   * @param {number} target
   * @return {number[]}
   */
  // bruteforce solution: use nested loop to try each permutation
  // TC: O(n^2) / SC: O(1)
  // twoSum(nums, target) {
  //     for(let i = 0; i < nums.length; i++) {
  //         for(let j = i + 1; j < nums.length; j++) {
  //             if (nums[i] + nums[j] == target) {
  //                 return [Math.min(i, j), Math.max(i,j)]
  //             }
  //         }
  //     }
  // }

  // optimized solution: use set to store compliment then check if compliment exist
  // TC: O(n) / SC: O(n)
  twoSum(nums, target) {
    const compliments = {};

    for (let i = 0; i < nums.length; i++) {
      const compliment = target - nums[i];
      if (compliment in compliments) {
        return [compliments[compliment], i];
      }
      compliments[nums[i]] = i;
    }
  }
}
