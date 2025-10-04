class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        sub = []
        for x in nums:
            i = bisect_left(sub, x)
            if i == len(sub):
                sub.append(x)
            else:
                sub[i] = x
        
        return len(sub)




        