# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp1 = head if head != None else None
        temp2 = head.next if head != None else None

        while temp2 != None:
            if temp1.val == temp2.val:
                temp1.next = temp2.next
            else:
                temp1 = temp2  

            temp2 = temp2.next       

        return head    
            




        


        
    