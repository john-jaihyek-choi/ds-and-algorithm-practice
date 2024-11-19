import math

# Leetcode 1071:
class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Note:
            # input:
                # str1: str
                # str2: str
            # output:
                # output: str
            # goal:
                # given 2 strings, return the greater common divisor of strings
        # General idea:
            # if str1 + str2 == str2 + str1, it means the two strings could have a valid common divisor
            # if I use the gcd on the combined string (str1 + str2), the result should return common divisor length that would contain the smallest block of substring the entire string could be divided by
        # Pseudocode:
            # if str1 + str2 != str2 + str1:
                # return ""
            # find the greatest common divisor:
                # math.gcd(len(str1), len(str2))
        
        # TC: O(n) / SC: O(n)
        if str1 + str2 != str2 + str1: # O(n)
            return ""

        divisor = math.gcd(len(str1), len(str2)) # O(log( min(n1, n2))) but approximates to O(1) since string operation dominates

        return str1[0:divisor] # O(k) where k = length of substring
    

class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # input:
            # str1: str
            # str2: str
            # * str1 and str2 both consists of UPPERCASE LETTERS
        # goal: return the largest string x such that x divides both str1 and str2
            # Because the goal is the to find the greatest common divisor of both strings:
                # all string of the shorter string MUST be present in the longer string for it to be a greatest common divisor
        # Brainstorm:
            # 1. Find common prefix of the two strings
                # Taking the shorter of the two strings, then iterating on the longer string for matching substring
                # find the string with shorter length
                # check if the prefix of the longer string (long_str[0:len(str2)]) is equal to each other
                    # if equals, commo prefix is found
                    # if it doesn't match, the string doesn't have common prefix
            # 2. Find the greatest common divisior string of of the two strings
        # Solution:
            # 1. Finding common prefix and checking if all strings match:
                # finding common prefix in this example is trivial since we are working with str and in order for string to share common divisor, concatenated value of str1 and str2, and str2 and str1 must equal to each other
                # this takes care of the finding the common prefix and ensuring both letters can be divided by its greatest common divisor
            # 2. getting the gcd of the prefix
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_len = math.gcd(len(str1), len(str2))
        
        return str1[:gcd_len]
                

