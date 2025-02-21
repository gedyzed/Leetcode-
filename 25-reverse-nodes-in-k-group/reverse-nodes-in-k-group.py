# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(curr, last):
            next, prev = last.next, None
            temp_head = curr
            count = 0
            
            while curr and count < k:
                temp = curr
                curr = curr.next
                temp.next = prev
                prev = temp
                count += 1

            # Connect the remaining elements  
            temp_head.next = next  
            return prev, temp_head  

        if k == 1:
            return head

        count, curr = 0, None
        last = head
        new_head = None

        while last:
            count += 1

            if count == k:
                temp = last.next
                if not curr:
                    new_group, prev_tail = reverse(head, last)
                    new_head = new_group
                else:  
                    new_group, prev_tail = reverse(curr.next, last)
                    curr.next = new_group

                curr = prev_tail
                last = temp
                count = 0
            else:       
                last = last.next  

        return new_head if new_head else head