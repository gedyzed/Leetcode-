class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []
        nums.sort()
        for left in range(len(nums)):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                if nums[left] + nums[middle] + nums[right] == 0:
                    answer.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    while nums[middle] == nums[middle-1] and middle < right:
                        middle += 1
                elif nums[left] + nums[middle] + nums[right] < 0:  
                    middle += 1
                else: 
                    right -= 1     
                   
        return answer




        