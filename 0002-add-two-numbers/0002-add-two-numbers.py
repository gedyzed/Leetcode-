# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = self.getNums(l1)
        nums2 = self.getNums(l2)

        add = self.mergeNums(nums1) + self.mergeNums(nums2) 
        nums = str(add)

        head = None 
        for i in range(len(nums) - 1, -1 , -1):
            if head == None:
                n = ListNode(int(nums[i])) 
                head = n
            else:
                temp = head
                while temp.next != None:
                    temp = temp.next
                n = ListNode(int(nums[i])) 
                temp.next = n        

        return head

    def getNums(self, node):
        temp = node
        nums = []
        while temp != None:
            nums.append(temp.val)
            temp = temp.next
        return nums  
    
    def mergeNums(self, nums):
        nums1 = 0
        for i in range(len(nums)) :
            nums1 += nums[i] * 10 ** i    
        return nums1       