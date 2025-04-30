# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        res = []
        for list in lists:
            while list:
                res.append(int(list.val)) 
                list = list.next

        res.sort()  
        dummy = ListNode(0) 
        curr = dummy
        for val in res:
            curr.next = ListNode(val)
            curr = curr.next

        curr.next = None
        return dummy.next        

        