# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
        dummy = ListNode(0, head)
        temp1 = dummy
        temp2 = temp1.next if temp1 != None else None

        while temp2 != None:
            if temp2.val == val:
                temp1.next = temp2.next
                temp2 = temp1.next if temp1 != None else None
            else:
                temp1 = temp2
                temp2 = temp2.next if temp1 != None else None

        return dummy.next   

