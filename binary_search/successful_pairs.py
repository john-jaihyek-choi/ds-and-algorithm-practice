from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time, math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # input:
            # spells: List[int]
                # spells[i] is the strength of the spell
            # potions: List[int]
                # potions[i] is the strength of the potion
            # success: int
                # the target for the product of spell and potions
            # note:
                # n = len(spells)
                # m = len(potions)
                # n, m are both atleast 1 or upto 100,000
                # success atleast 1 or upto 10,000,000,000
        # goal:
            # return an array, pairs, that contians the number of successful potion/spell pair
                # pairs[i]: int
                    # pairs[i] is the total number of potions that are a successful pair with spell[i]
        # Brainstorm:
            # Bruteforce:
                # iterate on spells
                    # iterate every i at potions for a "successful" pair
                # O(n^2) time and O(n) space operation
            # Optimal Solution:
                # Binary search:
                    # Assuming sorting using the built-in function is allowed
                        # I can sort the potions array
                            # Assuming in-place sorting is allowed
                                # use .sort()
                            # Assuming in-place sorting is not allowed
                                # use sorted and assign it to a variable
                    # iterate on spells
                        # do a binary search on the potions array
                            # set left and right bound
                            # set mid point
                            # compute the minimum potion strength (math.ceil(success / spell))
                                # if minimum potion strength greater than potions[m]
                                    # check the right half
                                # if minimum potion strength less than or equal to potions[m]
                                    # check the left half
                                # compute the total possible number of potions:
                                    # mid represents the index of the potions array
                                        # len(potions) - mid + 1 (for 0-indexed) will represent the number of potions that are greater than potions[mid]
                                # append the total number of potion to the pairs array
        # Variable:
            # pairs: List[int]
                # pairs[i] = number of successful potion pair with spell[i]
        # Pseudocode:
            # initialize pairs array
                # pairs = []
            # sort the potions array in-place
                # potions.sort()
            # iterate on the spells array (i = index, spell = spells[i])
                # initialize the left and right bound for binary search
                    # l, r = 0, len(potions)
                # initialize a minimum_potion_strength
                    # math.ceil(success / spell)
                # start binary searching:
                    # while l <= r:
                        # m = (l + r) // 2
                        # if potions[m] >= minimum_potion_strength
                            # r = m - 1
                        # if potions[m] < minimum_potion_strength
                            # l = m + 1
                        # compute the possible number of potions:
                            # successful_potions = len(potions) - m + 1
                        # pairs.append(successful_potions)
            # return pairs
        pairs = []
        potions.sort()
        
        for i, spell in enumerate(spells):
            min_potion_strength = math.ceil(success / spell)
            
            l, r = 0, len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                if potions[m] >= min_potion_strength:
                    r = m - 1
                else:
                    l = m + 1
                
            successful_potions = len(potions) - l
            pairs.append(successful_potions)
        
        return pairs

solution = Solution()
start_time = time.time()
print(solution.successfulPairs([-1,0,2,4,6,8], 0))
print("--- %s seconds ---" % (time.time() - start_time))