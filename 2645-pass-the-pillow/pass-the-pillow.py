class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        result = [num for num in range(1, n + 1 )]

        if time <= n - 1:
            return result[time]    
        q = time // (n - 1)  
        idx = time % (n - 1)

        if q % 2 == 0:
            return result[idx]
        return result[n - idx - 1]
 