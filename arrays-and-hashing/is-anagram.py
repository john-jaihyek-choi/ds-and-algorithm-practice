from typing import List


def isAnagram(s: str, t: str) -> bool:
    # if length of string s is not equal to t, return false
    # create a hash map that for the count of strings for both s and t
    # iterate over length of either string many times and add value at each index as a key to the hashmaps

    if len(s) != len(t):
        return False
    
    mapS, mapT = {}, {}

    for i in range(len(s)):
        mapS[s[i]] = 1 + mapS.get(s[i], 0)
        mapT[t[i]] = 1 + mapT.get(t[i], 0)
    return mapS == mapT

print(isAnagram("racecar", "carrace"))
print(isAnagram("jar", "jam"))