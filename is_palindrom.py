from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def isPalindrome(s: str) -> bool:
    # Note:
        # case insensitive
        # can ignore non-alphanumeric characters
    # Pseudocode:
        # initialize a formatted string from the input s (formatted_s)
            # lowercase each letter
            # ignore non-alphanumeric characters
        # initialize left and the right pointer (l, r)
        # iterate the formatted_s string while l < r
            # if string[l] == string[r]
                # increment l by 1 and decrement r by 1
            # else return false
        # return true if loop completes without exiting

    # Solution 1:
    # formatted_s = ''

    # for c in s:
    #     if c.isalnum():
    #         formatted_s += c.lower()

    # l = 0
    # r = len(formatted_s) - 1

    # while l < r:
    #     if formatted_s[l] != formatted_s[r]:
    #         return False
    #     l += 1
    #     r -= 1

    # return True

    # Solution 2:
    formatted_s = ''

    for c in s:
        if c.isalnum():
            formatted_s += c.lower()

    return formatted_s == formatted_s[::-1]

    # Solution 3:

start_time = time.time()
print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("tab a cat"))
print("--- %s seconds ---" % (time.time() - start_time))