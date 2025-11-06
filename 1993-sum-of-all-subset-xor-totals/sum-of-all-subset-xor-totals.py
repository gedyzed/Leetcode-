class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(idx, xor):
            res = xor
            for i in range(idx, len(nums)):
                res += backtrack(i + 1, xor ^ nums[i])
            return res

        return backtrack(0, 0)