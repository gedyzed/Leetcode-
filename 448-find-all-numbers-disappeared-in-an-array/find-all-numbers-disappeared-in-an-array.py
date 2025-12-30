class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums_, ans = set(nums), []
        for num in range(1, len(nums) + 1):
            if num not in nums_:
                ans.append(num)
        
        return ans
  