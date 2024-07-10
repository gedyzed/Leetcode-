class Solution:
    def arrangeCoins(self, n: int) -> int:  
        left = 1
        right = n

        while left <= right :
            mid = (left + right)//2
            total = (mid*(mid+1))//2
    
            if total == n:
                return mid  
            elif n < total:
                right = mid-1
            else:
                left = mid +1
                
        return right