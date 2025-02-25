# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # get the middle element
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the other mid
        prev = None
        while slow:
            temp = slow
            slow = slow.next

            temp.next = prev
            prev = temp 

        reversed = prev

        # find max twin sum
        max_sum = 0
        while head and reversed:
            sum = head.val + reversed.val
            max_sum = max(max_sum, sum)

            head = head.next 
            reversed = reversed.next

        return max_sum    


            

