class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Objective: given string s that represents roman numeral, return the numeric value

        Ideas:
            1. Initial thought solution: keep unique symbol to value mapping using hashmap, iterate and add each values
                - special conditions:
                    - if I is before V or X, subtract V or X by 1
                    - if X is before L or C, subtract L or C by 10
                    - if C is before D and M, subtract D or M by 100
                - pseudocode:
                    - initialize a proper roman numeral mapping (symbols)
                    - initialize res to 0
                    - iterate on s (c = s[i])
                        - nxt = s[i+1] if i < len(s) else None
                        - if c == 'I' && nxt == "V" or nxt == "X":
                            - res += symbols[nxt] - 1
                        - elif c == 'X' && nxt == "L" or nxt == "C":
                            - res += symbols[nxt] - 10
                        - elif c == 'C' && nxt == "D" or nxt == "M":
                            - res += symbols[nxt] - 100
                        - else:
                            - res += symbols[c]
                    - return res
        """

        # TC: O(n) / SC: O(k) where k == unique symbols
        # TC could be O(1) due to constraint roman numeral in the range [1, 3999].
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        for i, c in enumerate(s):
            nxt = s[i + 1] if i < len(s) - 1 else None
            if c == "I" and (nxt == "V" or nxt == "X"):
                res -= 1
            elif c == "X" and (nxt == "L" or nxt == "C"):
                res -= 10
            elif c == "C" and (nxt == "D" or nxt == "M"):
                res -= 100
            else:
                res += symbols[c]
        return res

        # Cleaner, more dynamic approach:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i, cur in enumerate(s):
            nxt = s[i + 1] if i < (len(s) - 1) else None

            if nxt and symbols[cur] < symbols[nxt]:
                res -= symbols[cur]
            else:
                res += symbols[cur]

        return res

        # Predefining all posible symbols:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        res = 0
        i = 0
        while i < len(s):
            cur = s[i]
            nxt = s[i + 1] if i < (len(s) - 1) else None

            if nxt and symbols[cur] < symbols[nxt]:
                res += symbols[cur + nxt]
                i += 2
            else:
                res += symbols[cur]
                i += 1

        return res
