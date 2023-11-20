# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        queue = res
        lists = list(filter(None, lists))
        while len(lists) != 0:
            mv, mi = min((l.val, i) for i, l in enumerate(lists))
            queue.next = ListNode(val=mv)
            queue = queue.next
            if lists[mi].next is None:
                del lists[mi]
            else:
                lists[mi] = lists[mi].next
        return res.next
