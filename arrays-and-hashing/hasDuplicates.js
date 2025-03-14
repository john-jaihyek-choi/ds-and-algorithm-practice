class Solution {
  // TC: O(n) / SC: O(1)
  hasDuplicate(nums) {
    const new_nums = new Set();

    for (const num of nums) {
      if (new_nums.has(num)) {
        return true;
      }
      new_nums.add(num);
    }

    return false;
  }
}
