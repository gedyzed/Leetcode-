class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numsHash = {}
        for i in range(len(nums)):
            if nums[i] in numsHash :
                return True
            numsHash[nums[i]] = i
        return False         



        