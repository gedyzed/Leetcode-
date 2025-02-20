# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-101, head)
        left, right = dummy, dummy.next

        while right:
            if left.val == right.val:
                left.next = right.next
            else:
                left = right  

            right = right.next     

        return dummy.next    
            




        


        
    