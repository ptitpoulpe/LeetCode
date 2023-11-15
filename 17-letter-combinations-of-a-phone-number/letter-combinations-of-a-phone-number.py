class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "0": " ",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits == "":
            return []
        res = [""]
        for digit in digits:
            res = [
                i + v
                for i in res
                for v in keyboard[digit]
            ]
        return res
