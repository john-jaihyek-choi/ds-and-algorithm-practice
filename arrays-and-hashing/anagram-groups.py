from collections import defaultdict
from typing import List
import time

# Leetcode 49


class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # objective:
        # given array of strings, strs, return the grouped anagrams
        # keywords:
        # anagram:
        # word or phrase formed by rearranging the letters of different word or phrase using all the original letters exactly once
        # condition:
        # same length
        # same frequency of appearance of letters
        # grouped anagram
        # array of arrays where arrays[i] contains the array of words that are in the same anagram group
        # brainstorm:
        # bruteforce solution:
        # use dictionary to store unique sorted str
        # iterate on strs:
        # for each str, sort str
        # if sorted str is in dictionary, append original str to the existing array
        # else, create a new array with original str in it
        # this solution is inefficient as it is O(n * m log m) time complexity
        # optimal solution:
        # use dictionary to store unique tuple sequence of strs (grouped_anagrams)
        # contraint says strs[i] is consisted of only english lowercase letters (26 characters)
        # put empty array as a default value
        # iterate on strs: (str = strs[i])
        # initialize empty array with size 26 with 0 as a default value (hash_key)
        # iterate on each str: (c = str[i])
        # update hash_key[ord(c) - ord("a")] += 1
        # if hash_key in grouped_anagrams:
        # grouped[hash_key].append(str)
        # else:
        # grouped_anagrams[hash_key] = [str]
        # return the values of the grouped_anagram dictionary

        # TC: O(n * k) / SC: O(n * k)
        # where k = len(word)
        grouped_anagrams = defaultdict(list)
        for word in strs:
            hash_key = [0] * 26

            for c in word:
                hash_key[ord(c) - ord("a")] += 1

            grouped_anagrams[tuple(hash_key)].append(word)

        return list(grouped_anagrams.values())

        # not using default dict
        grouped_anagrams = {}
        for word in strs:
            hash_key = [0] * 26

            for c in word:
                hash_key[ord(c) - ord("a")] += 1

            if tuple(hash_key) in grouped_anagrams:
                grouped_anagrams[tuple(hash_key)].append(word)
            else:
                grouped_anagrams[tuple(hash_key)] = [word]

        return list(grouped_anagrams.values())


# retried 3/14/2025
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # bruteforce: sort words in strs, then
        # TC: O(n * klogk) / SC: O(n)
        # anagrams = defaultdict(list)

        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     anagrams[sorted_s].append(s)

        # return [anagram for anagram in anagrams.values()]

        # optimized solution:
        # idea:
        # instead of sort:
        # define 26 length of array with 0s
        # for each word, turn string into array hash
        # set tuple(array hash) to res
        # use defaultdict(list) for easy push to default empty list
        # Pseudocode:
        # res = defaultdict(list)
        # for str in strs:
        # str_hash = [0] * 26
        # for c in str:
        # str_hash[ord(c) - ord("a")] += 1
        # res[tuple(str_hash)].append(str)
        # TC: O(n * m) / SC: O(n)
        hashmap = defaultdict(list)
        for s in strs:
            str_hash = [0] * 26
            for c in s:
                str_hash[ord(c) - ord("a")] += 1
            hashmap[tuple(str_hash)].append(s)

        return [items for items in hashmap.values()]


class Solution1:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        # initial solution:
        # initiate a empty response array
        # create a hash map to store the grouped anagrams
        # iterate over the list array
        # for each word in an array, count the numbers of each character, then store it in the hash map
        # hash the hashmap of the character counts and add it to the grouped anagram hash map in an array
        # After the iteration is complete, iterate over grouped anagram hashmap, and items in each key to a response array

        # res_arr = []
        # anagram_group = {}

        # for word in strs:
        #     char_count = {}
        #     for char in word:
        #         char_count[char] = 1 + char_count.get(char, 0)

        #     print(f'char_count: {char_count}')
        #     hashed_count = hash(str(sorted(char_count.items())))

        #     if hashed_count in anagram_group:
        #         anagram_group[hashed_count].append(word)
        #     else:
        #         anagram_group[hashed_count] = [word]

        # for group in anagram_group:
        #     res_arr.append(anagram_group[group])

        # return res_arr

        # solution 2:
        # create a dictionary which to store the grouped anagrams
        # iterate over the list array
        #     create an array called count_array with 26 in length (a-z = 26 characters) each index starting off from 0
        #     iterate each characters in a word
        #         increment the count_array[i] by 1
        #     add the count_array as a key to the grouped_anagram dictionary

        # print the contents of the hash map dictionary

        res_arr = defaultdict(list)

        for word in strs:
            count_arr = [0] * 26

            for char in word:
                char_index = ord(char) - ord("a")
                count_arr[char_index] += 1

            res_arr[tuple(count_arr)].append(word)

        return res_arr.values()


start_time = time.time()
solution = Solution3()
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
print("--- %s seconds ---" % (time.time() - start_time))

# print(groupAnagrams(["x"]))
