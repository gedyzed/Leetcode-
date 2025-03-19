class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path):

    
            if len(path) == len(nums):
                res.append(path[:]) 
                return 

            for i in range(len(nums)):

                if nums[i] in path:
                    continue

                path.append(nums[i])
                backtrack(path)  
                path.pop()  

        res = []
        backtrack([])   
        return res     
