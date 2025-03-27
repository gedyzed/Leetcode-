class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def validate(force):
            num_b, pos = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - pos >= force:
                    num_b += 1
                    pos = position[i]
                
            return num_b >= m  

        position.sort()         
        low, high = 1, position[-1] - position[0]
        while low <= high:
            mid = (low + high ) // 2
            if validate(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high            

      
        