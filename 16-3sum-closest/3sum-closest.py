class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        sum = closest_sum =  0
        closest =  float('inf')
        for left in range(len(nums)):
            middle, right = left + 1, len(nums) - 1  
            while middle < right:
                sum = nums[middle] + nums[right] + nums[left]
                if abs(sum - target) < closest:
                    closest_sum =  sum
                    closest = abs(sum - target)

                if sum == target:
                   return sum
                elif sum < target:
                    middle += 1
                else:
                    right -= 1

        return closest_sum            



             
           



                

        