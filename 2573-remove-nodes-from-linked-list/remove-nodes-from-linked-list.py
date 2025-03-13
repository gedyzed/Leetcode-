# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        curr, max_ = dummy, 0
        
        def removeNode(prev, curr):

            if not curr:
                return 0
            
            max_ = max(curr.val, removeNode(prev.next, curr.next))
            if curr.val < max_:
                prev.next = prev.next.next

            return max_     

        removeNode(curr, curr.next)
        return dummy.next

        