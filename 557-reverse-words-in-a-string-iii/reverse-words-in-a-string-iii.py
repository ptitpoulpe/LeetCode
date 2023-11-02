class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join("".join(reversed(w)) for w in s.split(" "))