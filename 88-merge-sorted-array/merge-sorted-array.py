class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = 0
        for left in range(m, len(nums1)):
            nums1[left] = nums2[right]
            right += 1

        nums1.sort()    


        