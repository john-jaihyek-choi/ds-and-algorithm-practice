class Solution {
  /**
   * @param {string} s
   * @param {string} t
   * @return {boolean}
   */
  // bruteforce solution - sort and compare
  // TC: O(nlogn) / SC: O(n)
  // isAnagram(s, t) {
  //     if (s.split("").sort().join() == t.split("").sort().join()) {
  //         return true
  //     }

  //     return false
  // }

  // optimized solution - hash letter to count then compare
  // TC: O(n) / SC: O(26) == O(1)
  // isAnagram(s,t ) {
  //     if (s.length !== t.length) {
  //         return false
  //     }

  //     const s_count = {}
  //     const t_count = {}

  //     for (let i = 0; i < s.length; i++) {
  //         s_count[s[i]] = (s_count[s[i]] || 0) + 1
  //         t_count[t[i]] = (t_count[t[i]] || 0) + 1
  //     }

  //     for (const c in s_count) {
  //         if (t_count[c] !== s_count[c]) {
  //             return false
  //         }
  //     }

  //     return true
  // }

  // optimized solution with charcode
  isAnagram(s, t) {
    if (s.length !== t.length) {
      return false;
    }

    const letters = Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
      letters[s.charCodeAt(i) - "a".charCodeAt(0)]++;
      letters[t.charCodeAt(i) - "a".charCodeAt(0)]--;
    }

    for (const l of letters) {
      if (l !== 0) {
        return false;
      }
    }

    return true;
  }
}
