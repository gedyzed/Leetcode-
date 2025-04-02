# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        vals.sort()  
        if not vals: 
            return head 

        head = ListNode(vals[0])
        curr = head
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next

        curr.next = None
        return head.next    


        