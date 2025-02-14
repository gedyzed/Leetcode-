class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        sum = 0
        closest =  float('inf')
        closest_sum = {}
        for left in range(len(nums)):
            middle, right = left + 1, len(nums) - 1  
            while middle < right:
                sum = nums[middle] + nums[right] + nums[left]
                closest = min(abs(sum - target), closest) 
                if closest in closest_sum:   
                    if abs(sum - target) >= abs(closest_sum[closest] - target):
                        closest_sum[closest] = closest_sum[closest]  
                    else:
                        closest_sum[closest] = sum
                else:
                    closest_sum[closest] = sum

                if sum == target:
                    middle += 1
                    right -= 1
                elif sum < target:
                    middle += 1
                else:
                    right -= 1
        return closest_sum[closest]            



             
           



                

        