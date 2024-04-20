class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1

        if len(nums) == 1:
            return nums[0]

        while left <= right:
            mid = (left + right )//2 
            if mid == 0 and nums[mid] != nums[mid + 1] :
                return nums[mid]
            elif mid == right and nums[mid-1] != nums[mid]:
                return nums[mid]
            elif nums[mid] != nums[mid+1] and nums[mid] != nums[mid - 1] and mid % 2 == 0:
                    return nums[mid] 
            elif nums[mid] == nums[mid + 1] and (mid +1) % 2 == 0 or nums[mid-1] == nums[mid] and  mid % 2 == 0:
                right = mid -1
            else:
                 left = mid + 1  
        



        