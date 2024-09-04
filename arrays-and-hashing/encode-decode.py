from collections import defaultdict
from typing import List
import time

def encode(strs: List[str]) -> str:
    # simple encryption approach - adding number of characters before the start of each word
    # initialize a string which to store the encrypted text (encrypted_text)
    # iterate the strs list and for each word, append the len of the word to the encrypted_text, AND append the actual characters of the word
    # return the encrypted_text

    encrypted_text = ''

    for str in strs:
        encrypted_text += f'{len(str)}#{str}'

    return encrypted_text


def decode(s: str) -> List[str]:
    # example input: [4#neet4#code4#love3#you]
    # iterate over the argument "s" starting at 0th index
        # get the substring of the s between s[i+1:i+s[i]]
    
    res_list = []

    i = 0
    while i < len(s):
        j = i

        while s[j] != "#":
            j += 1

        word_length = int(s[i:j])

        i = j + 1 # index of the first char of the word
        j = i + word_length # index of the last char of the word
        word = s[i:j]

        res_list.append(word)

        print(word)

        i = j # set a new starting point for i

    return res_list

start_time = time.time()
encoded = encode(["neetdjhflajkdhsflahsdlfhalsdf","code","love","you"])
print(encoded)
print(decode(encoded))
print("--- %s seconds ---" % (time.time() - start_time))

