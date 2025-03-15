class Solution {
  /**
   * @param {string[]} strs
   * @return {string[][]}
   */
  // bruteforce solution: sort each words, set each sorted word as hash key
  // TC: O(n * klogk) / SC: O(n)
  groupAnagrams(strs) {
    // steps:
    // defined hashmap
    // iterate on strs
    // sort the word
    // take the worted word register to hashmap
    // if already exists:
    // append str to the existing value
    // else:
    // create a new array with str as the 0th value
    // iterate on the hashmap
    // append all values in hashmap to res (Array)
    const hashmap = {};
    for (const word of strs) {
      const sorted_word = word.split("").sort().join("");
      if (sorted_word in hashmap) {
        hashmap[sorted_word].push(word);
      } else {
        hashmap[sorted_word] = [word];
      }
    }

    const res = [];
    for (const words of Object.values(hashmap)) {
      res.push(words);
    }

    return res;
  }

  // optimized solution: set array for array hashing
  groupAnagrams(strs) {
    // steps:
    // define hashmap for anagrams (hashmap)
    // iterate on strs (word = strs[index])
    // insantiate Array with 0 with length of 26 (arr_str)
    // iterate on each letter of the word (i = index, c = word[i])
    // arr_str[c.charCodeAt(i) - "a".charCodeAt(0)] by 1
    // if arr_str in hashmap:
    // hashmap[arr_str].append(word)
    // else:
    // hashmap[arr_str] = [word]
    // iterate on hashmap values and return the array of values

    const hashmap = {};
    for (const word of strs) {
      const arr_str = Array(26).fill(0);

      for (let i = 0; i < word.length; i++) {
        arr_str[word.charCodeAt(i) - "a".charCodeAt(0)]++;
      }

      if (arr_str in hashmap) {
        hashmap[arr_str].push(word);
      } else {
        hashmap[arr_str] = [word];
      }
    }

    return Object.values(hashmap);
  }
}
