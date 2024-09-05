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

    # l, r = 0, len(formatted_s) - 1 

    # while l < r:
    #     if formatted_s[l] != formatted_s[r]:
    #         return False
    #     l += 1
    #     r -= 1

    # return True

    # Solution 2:
    # formatted_s = ''

    # for c in s:
    #     if c.isalnum():
    #         formatted_s += c.lower()

    # return formatted_s == formatted_s[::-1]

    # Solution 3:
    l, r = 0, len(s) - 1

    while l < r:
        # check if alpha numeric
        # check if lower vs upper
        while l < r and not is_alphanumeric(s[l]):
            l += 1
        while l < r and not is_alphanumeric(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    
    return True

def is_alphanumeric(c: str) -> bool:

    return (
        ord('A') <= ord(c) <= ord('Z')
        or ord('a') <= ord(c) <= ord('z')
        or ord('0') <= ord(c) <= ord('9')
    )

start_time = time.time()
print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("tab a cat"))
print("--- %s seconds ---" % (time.time() - start_time))