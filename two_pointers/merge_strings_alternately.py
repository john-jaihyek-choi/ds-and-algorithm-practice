# Leetcode 1768:

class Solution:
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

        # TC: O(m) where m is length of the longer word / SC: O(n + m)
        output = ""
        w1p, w2p = 0, 0
        while w1p < len(word1) or w2p < len(word2):
            w1_char = word1[w1p] if w1p < len(word1) else ""
            w2_char = word2[w2p] if w2p < len(word2) else ""

            output += w1_char + w2_char
            w1p += 1
            w2p += 1


        return output
        