class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        n, count = len(nums), 0

        for k in range(2, n):
            j, i = k - 1, 0
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:    
                    i += 1  

        return count          
    
             
            




        