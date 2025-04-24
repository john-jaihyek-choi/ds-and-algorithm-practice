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
        # string approach:
        if x < 0 or x % 10 == 0:
            return False

        num = str(x)
        l, r = 0, len(num) - 1

        while l < r:
            if num[l] != num[r]:
                return False
            l += 1
            r -= 1

        return True


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        """
        Math approach: rever then compare
        """
        # math approach (reverse then compare):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original = x
        reverted_num = 0

        while original > 0:
            reverted_num = (reverted_num * 10) + (original % 10)
            original //= 10

        return reverted_num == x


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        """
        Math approach: revert half then compare
        """
        # math approach (reverse half way then compare with another half):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_num = 0

        while x > reverted_num:
            reverted_num = (reverted_num * 10) + (x % 10)
            x //= 10

        return reverted_num == x or x == reverted_num // 10
