# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        queue = deque()
        head = ListNode(next=head)
        res = head
        while head.next is not None:
            queue.append(head)
            if len(queue) > n:
                queue.popleft()
            head = head.next
        print([e.val for e in queue])
        if len(queue) == 0:
            return None
        queue[0].next = None if len(queue) == 1 else queue[1].next
        return res.next