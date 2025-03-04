class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        
        steps, num = 0, 1
        while maxDoubles and target > 1:
            num = target // 2
            steps += target - num * 2 + 1
            maxDoubles -= 1
            target = num 
        
        return steps + target - 1    
                    
        