# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = ListNode()
        current = head

        while current:
            curr_min = lists[0]
            min_index = 0
            for i, l in enumerate(lists):
                if not l:
                    continue
                if not curr_min or l.val < curr_min.val:
                    curr_min = l
                    min_index = i
            current.next = curr_min
            current = current.next
            if lists[min_index]:
                lists[min_index] = lists[min_index].next

        return head.next
 
