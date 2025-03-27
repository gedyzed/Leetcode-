class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(left, right):

            if left > right:
                return -1
                
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid    
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

            return binarySearch(left, right) 

        left, right = 0, len(nums) - 1
        return binarySearch(left, right)
        