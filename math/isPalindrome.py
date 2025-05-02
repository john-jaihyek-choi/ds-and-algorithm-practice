import math


# Leetcode 9:
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        """
        Note:
            - if negative number, immediately False
                - negative sign always comes to the left of the number, so it can't be a palindrome
            - if number ends with 0, immediately False
                - number cannot have a trailing 0, so if...
                    - x % 10 == 0, it can't make a palindrome
        Intuition:
            - string approach:
                - transform x to string, then check if palindrome
                    - if negative number, immmediately false
            - math approach (reverse then compare):
                - if negative number, immediately false since they can never be palindrome due to - sign
                - repetitively modulo number by 10 (x % 10) on x, then add x % 10 to the reverted number(reverted number starting at 0)
                    - each iteration...
                        - reverted_number = reverted_number * 10 + x % 10
                            - x % 10 adds 10th place each time reverted_number changes
        """
        # TC: O(n) / SC: O(n)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        string_num = str(x)
        l, r = 0, len(string_num) - 1

        while l < r:
            if string_num[l] != string_num[r]:
                return False
            l += 1
            r -= 1

        return True


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        """
        Math approach: rever then compare
        """
        # TC: O(n) / SC: O(1)
        x_copy = x
        reverted_number = 0
        while x_copy > 0:
            reverted_number = reverted_number * 10 + (x_copy % 10)
            x_copy //= 10

        return reverted_number == x


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        """
        Math approach: revert half then compare with original half
        """
        # TC: O(n / 2) == O(n) / SC: O(1)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        copy = x
        reversed_num = 0
        while copy > reversed_num:
            # compute the last place of the number
            last_place = copy % 10
            copy //= 10
            reversed_num = (reversed_num * 10) + last_place

        return reversed_num == copy or reversed_num // 10 == copy
