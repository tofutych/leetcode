class Solution(object):
    def isPalindrome(self, x):
        if x == 0:
            return True
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        result = 0
        while x > result:
            result *= 10
            result += x % 10
            x //= 10

        return x == result or x == result // 10
