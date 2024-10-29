import math, time, os, random, sys, re
from collections import defaultdict, OrderedDict

# Leetcode 1268:

# Initial Try:
class Solution:
    def searchSuggestions(self, products, searchWord):
        # Write your code here
        # input: 
            # repository: List[str]
                # repository array containing the related query of the customerQuery
            # customerQuery: str
                # customer's query typed to the search bar
        # output:
            # List[ List[str] ]
                # where List[i] consists of list of related query at i
                    # ** only start related search after 2 characters **
                # Note:
                    # output at each index should be sorted in an alphabetical order
        # goal:
            # return a list of list of strings in lower case where:
                # each list represents keyword suggestions made by the system as the customer types each character
                # Assumed the customer types characters in order without deleting or removing any characters

        # Brainstorm:
            # Potential edge-cases:
                # empty query?
                    # return []
                # query unrelated to the strings in the repository?
                    # return []
            # General idea:
                # 1. sort the repository (Assuming sorting is allowed and built-in sort is allowed)
                # 2. iterate the customerQuery input
                    # as iterating, keep record of the query at each index
                        # uses a str variable to append each characters to
                # 3. search, in the sorted array, for the keyword as iterating:
                    # start searching after two characters (i >= 2)
                # 4. append the searched query result to the output/res array
        
        # Bruteforce Solution:
        # Variables:
            # res: List[ List[str] ]
            # query: str
                # substring of the customerQuery at each index
        # Pseudocode:
            # initialize an empty res array to store the query results in (res)
            # initialize an empty string to store the substring of customerQuery at each index (query)
            # sort the repository input (Assuming sorting in-place is allowed)
            # iterate the customerQuery string (i = index, c = customerQuery[i])
                # append c to query string
                # if len(query) string is >= 2:
                    # initialize an empty list to store the query result (query_res)
                    # search the query in an array
                        # iterate the repository and append the matching words to query_res (j = index, word = repository[j]):
                            # if word[:i].lower() == query.lower()
                                # append the word to query_res
                # append the query_res to res array
            # return res

        # TC: O((n * m) + m log m ) / SC: 
        res = [] # O(1)
        query = "" # O(1)
        products.sort() # O(m log m) where m = len(products)

        for i, c in enumerate(searchWord): # O(n) where n = len(searchWord)
            query += c.lower() # O(1)

            query_res = [] # O(1)
            for j, word in enumerate(products): # O(m) where m = len(products)
                if word[:i+1].lower() == query: # O(1)
                    query_res.append(word) # O(1)
                
                if len(query_res) == 3: # O(1)
                    break

            res.append(query_res) # O(1)

        return res # O(1)



solution = Solution()
start_time = time.time()
print(solution.searchSuggestions(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
print("--- %s seconds ---" % (time.time() - start_time))