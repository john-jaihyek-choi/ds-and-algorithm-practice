import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 345:
class Solution2:
    def reverseVowels(self, s: str) -> str:
        # Note:
            # input:
                # s: str
            # output:
                # output: str
            # goal:
                # given string s, return an output string where orders of the vowel letters are reversed
        # edge-case scenarios:
            # empty string:
                # s.length will be atleast 1 char long
            # no vowels in string:
                # return string as it is
            # non alphabetic char:
                # leave the char in its position
            # upper or lower case:
                # leave the casing the same
        # general approach:
            # Two-pointer:
                # keep list of valid vowels in a set
                # left and right pointer 
                    # left from 0
                    # right from len(s) - 1
                # while l < r:
                    # if s[l] and s[r] is valid vowel:
                        # set s[l], s[r] = s[r], s[l]
                    # if s[r] not valid:
                        # r -= 1
                    # if s[l] not valid
                        # l += 1
        # Pseudocode:
            # output = list(s)
            # vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
            # l, r = 0, len(output) - 1
            # while l < r:
                # if output[l] in vowels and output[r] in vowels:
                    # output[l], output[r] = output[r], output[l]
                # if output[r] not vowels:
                    # r -= 1
                # if output[l] not in vowels:
                    # l += 1
            # return "".join(output)

        # TC: O(n) / SC: O(n)
        output = list(s) # O(n)
        vowels = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}) # O(k) = O(1)
        l, r = 0, len(output) - 1 # O(1)
        while l < r: # O(n)
            if output[l] in vowels and output[r] in vowels: # O(1)
                output[l], output[r] = output[r], output[l]
                l += 1
                r -= 1
            if output[r] not in vowels: # O(1)
                r -= 1
            if output[l] not in vowels: # O(1)
                l += 1
        
        return "".join(output) # O(n)
    
class Solution1:
    def reverseVowels(self, s: str) -> str:
        # input:
            # s: str
            # ** s is only ASCII char
        # goal: reverse all vowels (a, e, i, o, u) in the given string, then return the updated string
        # Braintorm:
            # Two-pointer approach:
                # Main consideration:
                    # string cannot be manipulated on flight
                        # requires tranformation to array 
                            # adds space 
                # have l and r pointer
                    # l from 0
                    # r from the end of the list
                # Considerations for l and r shift:
                    # Are both char at l and r vowels
                        # if both are vowels, switch the value
                        # if none are vowels, move both pointers
                        # if either are non-vowel, move the non-vowel pointer
                    # stop when l and r crosses (l >= r)
            # Variables to track:
                # s_arr: List[str]
                # l: int
                # r: int
                # vowels: set
            # Pseudocode:
                # initialize vowels set (vowels)
                # initialize s_arr with input s transformed as list (s_arr)
                # initialize l and r: (l, r)
                    # l starts 0
                    # r starts len(s) - 1
                # while l and r doesn't cross:
                    # if s[l] in vowels and s[r] in vowels:
                        # temp = s[l]
                        # s[l], s[r] = s[r], temp
                    # elif s[l] in vowels:
                        # r -= 1
                    # elif s[r] in vowels:
                        # l += 1
                    # else:
                        # l += 1
                        # r -= 1
                # return ''.join(s_arr)
            
            # TC: O(n) / SC: O(n)
            vowels = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
            s_arr = list(s)
            l, r = 0, len(s) - 1
            while l < r:
                if s_arr[l] in vowels and s_arr[r] in vowels:
                    temp = s[l]
                    s_arr[l], s_arr[r] = s_arr[r], temp
                elif s_arr[l] in vowels:
                    r -= 1
                    continue
                elif s_arr[r] in vowels:
                    l += 1
                    continue

                l += 1
                r -= 1
            
            return ''.join(s_arr)

solution = Solution2()
start_time = time.time()
print(solution.reverseVowels('IceCreAm'))
print("--- %s seconds ---" % (time.time() - start_time))