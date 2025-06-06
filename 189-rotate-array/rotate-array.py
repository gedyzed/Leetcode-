class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]  
                left += 1
                right -= 1

        n = k % len(nums) 
        reverse(0, len(nums) - 1)   
        reverse(n, len(nums) - 1)
        reverse(0, n - 1)



               

        