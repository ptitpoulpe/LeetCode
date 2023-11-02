class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        def toDigits(d):
            res = []
            while d:
                d, m = divmod(d, 10)
                res.append(m)
            return res
        digits = toDigits(x)
        for i in range(len(digits)//2):
            if digits[i] != digits[-1 - i]:
                return False
        return True