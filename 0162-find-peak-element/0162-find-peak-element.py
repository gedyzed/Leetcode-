class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
         
        while left < right:
            mid = (left + right)//2
     
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid    
            elif mid + 1 <= right and arr[mid+1] > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1 
        if right == -1:
            return 0        
        return right
        
        