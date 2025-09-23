class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False

        memo = set([0])
        target = sum(nums) // 2
        def dp(i, memo):
            if i < 0:
                return True if target in memo else False
            temp = set()
            for num in memo:
                if num + nums[i] == target:
                    return True
                temp.add(num + nums[i])
                temp.add(num)
            memo = temp
            
            return dp(i - 1, memo)

        return dp(len(nums) - 1, memo)
        
                       