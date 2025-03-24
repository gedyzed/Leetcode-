class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(ids):
            
            if len(res) == len(nums):
                if res not in result:
                    result.append(res[:])
                return 

            for i in range(len(nums)):
                if i in ids:
                    continue

                ids.add(i)
                res.append(nums[i])  
                backtrack(ids)
                ids.remove(i)
                res.pop()  


        result = []    
        res = []
        backtrack(set())
        return result

        