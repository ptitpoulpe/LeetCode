class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        current = 0
        for c in reversed(s):
            v = values[c]
            res += v if v >= current else -v
            current = v
        return res
