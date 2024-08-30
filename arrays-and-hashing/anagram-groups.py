from collections import defaultdict
from typing import List
import time


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
            char_index = ord(char) - ord('a')
            count_arr[char_index] += 1

        res_arr[tuple(count_arr)].append(word)
    
    return res_arr.values()




start_time = time.time()
print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print("--- %s seconds ---" % (time.time() - start_time))

# print(groupAnagrams(["x"]))