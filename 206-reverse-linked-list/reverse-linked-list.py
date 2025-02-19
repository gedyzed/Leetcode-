# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        head = None
        while curr:

            temp = curr
            curr = curr.next 

            temp.next = head
            head = temp

        return head

              








        