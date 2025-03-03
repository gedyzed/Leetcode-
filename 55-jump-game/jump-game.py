class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        reach = 0
        for i in range(n):
            if reach < i:
                return False

            cur_reach = i + nums[i]    
            reach = max(reach, cur_reach)
        return True
        


     
        