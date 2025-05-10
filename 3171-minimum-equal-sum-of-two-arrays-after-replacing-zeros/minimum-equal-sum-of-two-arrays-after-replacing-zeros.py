class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        z1 = nums1.count(0)
        z2 = nums2.count(0)

        sum1 += z1
        sum2 += z2

        if sum1 != sum2 and not z1 and not z2:
            return -1
        elif sum1 > sum2 and not z2:
            return -1
        elif sum2 > sum1 and not z1:
            return -1        

        return max(sum1, sum2)
     