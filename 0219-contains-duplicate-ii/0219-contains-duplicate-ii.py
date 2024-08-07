class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        numsHash = {}
        for right in range(len(nums)):
            if nums[right] in numsHash :
                if abs(numsHash[nums[right]] - right) <= k:
                    return True
            numsHash[nums[right]] = right
        return False    




      