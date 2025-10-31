class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        nums_set, ans = set(), []
        for num in nums:
            if num in nums_set:
                ans.append(num)
            nums_set.add(num)
        
        return ans
        