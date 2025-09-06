class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]
        cnt = 1
        for layer in range((n + 1) // 2):
            for ptr in range(layer, n - layer):
                result[layer][ptr] = cnt
                cnt += 1
          
            for ptr in range(layer + 1, n - layer):
                result[ptr][n - layer - 1] = cnt
                cnt += 1
           
            for ptr in range(n - layer - 2, layer - 1, -1):
                result[n - layer - 1][ptr] = cnt
                cnt += 1
            
            for ptr in range(n - layer - 2, layer, -1):
                result[ptr][layer] = cnt
                cnt += 1
                
        return result