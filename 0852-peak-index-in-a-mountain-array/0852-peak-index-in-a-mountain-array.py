class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        
        while left < right:
            mid = (left + right)//2

            if mid != 0 and arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid    
            if mid + 1 <= right and arr[mid+1] > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1 
        return right        
      