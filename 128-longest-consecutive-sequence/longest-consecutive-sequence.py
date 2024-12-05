class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_ = Counter(nums)
        max_len = 0
        for num in nums:
            count = 0
            if num - 1 not in nums_:
                while num in nums_:
                    count += 1
                    num += 1

                if count > max_len:
                    max_len = count
              
        return max_len                

               
              