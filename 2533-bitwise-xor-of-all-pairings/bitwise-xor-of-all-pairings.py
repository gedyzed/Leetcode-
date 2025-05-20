class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        def xor(nums):
            x = 0
            for num in nums:
                x ^= num

            return x    

        n1, n2 = len(nums1), len(nums2)
        if not (n1 & 1) and not (n2 & 1):
            return 0

        if (n1 & 1) and (n2 & 1):
            return xor(nums1) ^ xor(nums2)
        elif (n1 & 1):
            return xor(nums2)    

        return xor(nums1)     

      