# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr, carry = dummy, 0
        while l1 or l2 or carry:

            sum = carry
            sum = sum + l1.val if l1 else sum
            sum = sum + l2.val if l2 else sum          

            digit = sum % 10 
            node = ListNode(digit)
            curr.next = node
            curr = node
            
            carry = 1 if sum > 9 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next    


        