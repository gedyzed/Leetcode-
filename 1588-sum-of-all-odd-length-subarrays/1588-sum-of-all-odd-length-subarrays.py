class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        total_sum = 0
        
        for start in range(n):
            for length in range(1, n - start + 1, 2):
                end = start + length
                total_sum += prefix_sum[end] - prefix_sum[start]
        
        return total_sum
            