class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        nums1 = set([num for  num in range(left, right + 1)])
        nums2 = set()
        for nums in ranges:
            r = [num for num in range(nums[0], nums[1] + 1)]
            nums2 = nums2 | set(r)
             
        return nums1 <=  nums2

