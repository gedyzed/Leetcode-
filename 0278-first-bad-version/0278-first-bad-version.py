# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                 return mid
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1    
                  

        