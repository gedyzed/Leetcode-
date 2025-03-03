# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(l):
            prev = None
            while l:
                temp = l
                l = l.next

                temp.next = prev
                prev = temp

            return prev     

        dummy = ListNode(-1)
        curr = dummy

        l1, l2 = reverse(l1), reverse(l2)
        carry = sum = 0
        while l1 or l2 or carry:

            sum = carry
            sum = sum + l1.val if l1 else sum
            sum = sum + l2.val if l2 else sum

            digit = sum % 10 if sum > 9 else sum
            carry = 1 if sum > 9 else 0

            new_node = ListNode(digit)
            curr.next = new_node
            curr = new_node  

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return reverse(dummy.next)   
                
     