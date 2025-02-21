# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd_dummy, even_dummy = ListNode(0), ListNode(0) 
        odd, even = odd_dummy, even_dummy
        is_even = False

        while head:
            
            if not is_even:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next       
            head = head.next
            is_even = not is_even
          
        even.next = None
        odd.next = even_dummy.next 
        return odd_dummy.next    

        