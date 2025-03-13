# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def removeNode(prev, curr):

            if not curr:
                return 0
            
            max_right = removeNode(prev.next, curr.next)
            if curr.val < max_right:
                prev.next = curr.next

            return max(curr.val, max_right)    

        dummy = ListNode(0, head)  
        removeNode(dummy, head)
        return dummy.next

        