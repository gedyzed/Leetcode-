class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(idx, res):

            if res not in result:
                result.append(res[:])
            if len(res) == len(nums):
                return 

            for i in range(idx, len(nums)):
                res.append(nums[i])
                backtrack(i + 1, res)
                res.pop()
               
        result = []
        nums.sort()
        backtrack(0, [])
        return result            

        


        