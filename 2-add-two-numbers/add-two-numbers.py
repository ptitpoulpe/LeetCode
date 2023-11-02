# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_current = res
        carry = 0
        l1_current = l1
        l2_current = l2
        while True:
            # get values
            l1_val = 0 if l1_current is None else l1_current.val
            l2_val = 0 if l2_current is None else l2_current.val

            # compute result
            res_current.val = l1_val + l2_val + carry
            carry = int(res_current.val >= 10)
            if carry:
                res_current.val -= 10

            # return result
            if (l1_current is None or l1_current.next is None) and (l2_current is None or l2_current.next is None) and carry == 0:
                return res
            
            # prepare next step
            if l1_current is not None:
                l1_current = l1_current.next
            if l2_current is not None:
                l2_current = l2_current.next
            new = ListNode()
            res_current.next = new
            res_current = new
            
        