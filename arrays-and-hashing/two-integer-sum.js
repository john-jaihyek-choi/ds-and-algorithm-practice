var twoSum = function (nums, target) {
  /*
    Note:
        - exactly one solution
        - cannot use same element twice
        - return answer in any order
    Intuition:
        1. Bruteforce:
            - nested loops, i and j, then check if each sum equals target
            - if equals to target, return the pair
            - TC: O(n^2) / SC: O(1)
        2. Use Hashmap:
            - define a hashmap to store compliments
            - iterate on nums:
                - find complimenting value of nums[i] and target
                - if complimenting value is found in compliments object:
                    - return pairs
            - TC: O(n) / SC: O(n)
    */

  // Hashmap:
  const compliments = {};
  for (let i = 0; i < nums.length; i++) {
    const compliment = target - nums[i];

    if (compliment in compliments) {
      return [compliments[compliment], i];
    }

    compliments[nums[i]] = i;
  }

  return [0, 0];
};
