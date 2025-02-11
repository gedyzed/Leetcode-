class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        target_indices = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == target:
                target_indices.append(i)
        return target_indices        

        