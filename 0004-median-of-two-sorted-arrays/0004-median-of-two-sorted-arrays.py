class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums  = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n % 2 != 0:
            return nums[(n+1)//2-1]
        middleNumbers =  nums[n//2] + nums[n//2-1]   
        return  middleNumbers/2 


        