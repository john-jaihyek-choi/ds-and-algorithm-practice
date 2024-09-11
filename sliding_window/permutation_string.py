from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def checkInclusion(s1: str, s2: str) -> bool:
    # Note:
        # 2 strings, s1 and s2
        # if s2 has permutation of s1, return true, otherwise false.
        # permutation - arrangement or ordering of elements of a set into specific sequence or order

    # Solution proposals:
        # 1. sort s1, then take each sorted s2 substring to compare (TC: O(n * m log(m)) / SC: O(m))
        # 1. storing s1 letters in a set, then compare (TC: O(n^2) / SC: O(n))

    # Solution 1 (TC: O(n * m log(m)) / SC: O(m))
    sorted_s1 = "".join(sorted(s1))
    
    if len(s1) > len(s2):
        return False

    for i in range(0, len(s2)):
        sorted_substring = "".join(sorted(s2[i:(i + len(s1))]))  
        if sorted_substring == sorted_s1:
            return True

    return False

start_time = time.time()
print(checkInclusion("adc", "dcda"))
print("--- %s seconds ---" % (time.time() - start_time))