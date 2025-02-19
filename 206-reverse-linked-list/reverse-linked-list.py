# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        first = None
        while curr:
            temp = curr
            curr = curr.next 

            if first:
                temp.next = first
                first = temp
            else:
                first = temp
                first.next = None 

        return first

              








        