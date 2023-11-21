# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        top = 10**5
        heap = [(top if l is None else l.val, i) for i, l in enumerate(lists)]
        heapq.heapify(heap)

        res = ListNode()
        queue = res
        while heap:
            mv, mi = heapq.heappop(heap)
            if mv == top:
                break
            queue.next = ListNode(val=mv)
            queue = queue.next
            lists[mi] = lists[mi].next
            heapq.heappush(heap, (top if lists[mi] is None else lists[mi].val, mi))
        return res.next
