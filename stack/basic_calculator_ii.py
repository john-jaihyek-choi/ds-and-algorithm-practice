from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time
import re

# Leetcode 227


class Solution:
    def calculate(self, s: str) -> int:
        """
        Note:
            - given a valid mathematical expression s, return the properly evaluated value
            - constraints:
                - possible operations:
                    +
                    -
                    *
                    /
            - Basic arithemtic rules:
                - "*" and "/" should be prioritized
                - Then + and -
            - s can contain:
                - expressions
                - empty spaces
                - numbers
        Experimentation:
            1:
                - s = "3+2*2"
                - output = 7
            2:
                - s = " 3/2 "
                - output = 1
            3:
                - s = " 3+5 / 2 "
        Intuition:
            - Stack to store each digits and expressions
                - trim (remove white spaces) input s and split it by expressions
                - iterate on the splitted array:
                    - if array[i] is number:
                        - if expressions[-1] is * or / and array[i] is number:
                            - pop numbers[-1]
                            - if *:
                                - multiply by array[i]
                            - if /:
                                - divide by array[i]
                            - push the computed number to numbers array
                        - else:
                            - push to numbers array
                    - elif array[i] is expression:
                        - append the expression to expressions array
                - while numbers stack is non-empty and expressions stack is non-empty:
                    - pop 2 numbers
                        - first pop = right
                        - second pop = left
                    - pop expression
                    - if expression is +:
                        - left + right
                    - if expression is -:
                        - left - right
                    - append the computed item back to numbers array
                - return numbers[-1]
        """

        splitted = re.split(r"(\d+|[+\-*/])", s)
        numbers, expressions = [], []

        for item in splitted:
            if item.strip() == "":
                continue

            if item.isdigit():
                cur_num = int(item)
                if expressions and (expressions[-1] == "*" or expressions[-1] == "/"):
                    left = numbers.pop()
                    exp = expressions.pop()
                    if exp == "*":
                        total = round(left * cur_num, 0)
                    else:
                        total = left // cur_num

                    numbers.append(total)
                else:
                    numbers.append(cur_num)
            else:
                expressions.append(item)

        while numbers and expressions:
            right = numbers.pop()
            left = numbers.pop()
            exp = expressions.pop()

            if exp == "+":
                total = left + right
            else:
                total = left - right

            numbers.append(total)

        return numbers[-1]


start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
