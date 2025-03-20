class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(idx, subset):

            res.append(subset[:])
            if idx >= len(nums):
                return 

            for i in range(idx, len(nums)):
            
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        res = []
        backtrack(0, [])
        return res        


                     
        