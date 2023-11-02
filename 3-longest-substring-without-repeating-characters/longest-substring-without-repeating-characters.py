class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        from_, to_ = 0, 0
        for i in range(len(s)):
            if (f := s.find(s[i], from_, to_)) != -1:
                from_ = f + 1
            to_ += 1
            if (l := to_ - from_) > max_length:
                max_length = l
        return max_length
        