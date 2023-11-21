# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode(next=head)
        queue = res
        while True:
            if queue.next is None or queue.next.next is None:
                break
            tmp = queue.next
            queue.next = queue.next.next
            tmp.next = queue.next.next
            queue.next.next = tmp
            queue = queue.next.next
        return res.next