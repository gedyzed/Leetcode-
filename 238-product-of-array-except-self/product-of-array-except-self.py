class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        right_product = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i]

        prefix= 1
        for i, num in enumerate(nums):
            nums[i] = prefix * right_product[i + 1]
            prefix *= num

        return nums     

        