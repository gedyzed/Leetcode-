class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        n1, n2 = len(nums1), len(nums2)
        def xor(nums):
            print(nums)
            x = 0
            for num in nums:
                x ^= num
                
            return x    

    
        if n1 % 2 and n2 % 2:
            return xor(nums1) ^ xor(nums2)
        elif n1 % 2:
            return xor(nums2)    
        elif n2 % 2:
            return xor(nums1)   

        return 0     

      