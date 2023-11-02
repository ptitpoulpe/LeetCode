class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        potential_two_stack, two = [], float("-inf")

        for num in reversed(nums):
            if num < two:
                # we found a one
                return True
            while potential_two_stack and potential_two_stack[-1] < num:
                # we found a new maximized two (num is a three)
                two = potential_two_stack.pop()
            potential_two_stack.append(num)
        return False
            