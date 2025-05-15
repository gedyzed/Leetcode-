class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []
        for i in range(1 << n):
            res = []
            for j in range(n):
                if i & (1 << j):
                    res.append(nums[j])  
            result.append(res[:])  
        return result               





                     
        