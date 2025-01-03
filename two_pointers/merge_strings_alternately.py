# Leetcode 1768:


# 1/2/2025 recap
class Solution3:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # input:
            # word1: str
            # word2: str
        # output:
            # output: str
        # note:
            # len(word1) and len(word2) <= 100
            # word1 and word2 consists of lowercase eng letter
        # visualization:
            # ex) word1 = 'abc' word2 = 'pqr'
                # output = 'apbqcr'
        # ideas:
            # two-pointers:
                # instantitate an empty arry to store the result string (output)
                # iterate the length of the shorter word of the two (i=index)
                    # set c1 to word1[i] if i < len(word1)
                        # otherwise, set it to empty str
                    # set c2 to word2[i] if i < len(word1)
                        # otherwise, set it to empty str
                    # extend c1 and c2 to the output array
                # return the joined string of the output

        # TC: O(n) where n is the length of the longer word / SC: O(n + m)
        output = []
        for i in range(max(len(word1), len(word2))):
            c1 = word1[i] if i < len(word1) else ""
            c2 = word2[i] if i < len(word2) else ""
            
            output.extend([c1, c2])
        
        return ''.join(output)


class Solution3:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # TC: O(n) / SC: O(n + m)
        output = []
        n = max(len(word1), len(word2))

        for i in range(n):
            c1 = word1[i] if i < len(word1) else ""
            c2 = word2[i] if i < len(word2) else ""

            output.extend([c1, c2])
        
        return "".join(output)

class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # note:
            # input:
                # word1: str
                # word2: str
            # output:
                # output: str
            # goal:
                # given 2 words, return the merged string that is merged alternately
        # Edge-case:
            # empty word1 or word2?
                # ** contraint in the problem restricting empty word
                # if either is empty:
                    # return valid word
                # if both are empty:
                    # return nothing
            # if one word is longer than another:
                # append the remaining letters to the end of the output
        # General approach:
            # First-thought solution:
                # initialize an empty string output
                # iterate on longer of the two words
                    # alternately append word1[i] and word2[i] to the output
                        # handle the string out of index edge-case gracefully with if else
                # return the output

        # Pseudocode:
            # output = ""
            # n = max(len(word1), len(word2))
            # for i in range(n):
                # c1 = word1[i] if i < len(word1) else ""
                # c2 = word2[i] if i < len(word2) else ""
                # output.extend([c1, c2])
            # return output
        
        # TC: O(n^2) / SC: O(n + m)
        output = ""
        n = max(len(word1), len(word2))
        for i in range(n): # O(n)
            c1 = word1[i] if i < len(word1) else ""
            c2 = word2[i] if i < len(word2) else ""
            output += c1 + c2 # O(n) due to string concatenation
        return output
    

class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # input:
            # word1: str
            # word2: str
            # * word1 and word2 are consistsed of only english letters
        # goal: return merged string which contains the stings in word1 and word2 alternatingly
        # Obvious solution:
            # iterate the word1 and word2 together and form a new word
            # take what's leftover in either word1 or word2 and append the rest of it to the output
        # Brainstorm:
            # keep 2 pointers moving at the same pace
                # w1p
                # w2p
            # each char will be added to the output alternatingly - word[w1p] + word[w2p] order
            # what if one word is longer than the other?
                # we can handle a default value of the string when list is out of index to empty string
        # Variables to keep track:
            # output: str
            # w1p: int
            # w2p: int
        # pseudocode:
            # initialize an output with an empty string (output)
            # initialize w1p and w2p both at 0
            # while w1p < len(word1) or w2p < len(word2):
                # w1_char = word1[w1p] if w1p < len(word1) else ""
                # w2_char = word2[w2p] if w2p < len(word2) else ""
                # append the w1_char + w2_char to the output in that order
                # increment w1p and w2p by 1
            # return the output

        # TC: O(n^2) / SC: O(n + m)
        output = ""
        w1p, w2p = 0, 0
        while w1p < len(word1) or w2p < len(word2):
            w1_char = word1[w1p] if w1p < len(word1) else ""
            w2_char = word2[w2p] if w2p < len(word2) else ""

            output += w1_char + w2_char
            w1p += 1
            w2p += 1


        return output
        