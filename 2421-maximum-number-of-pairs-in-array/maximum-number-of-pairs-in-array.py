class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        pairs = defaultdict(int)
        pair_count = 0
        for num in nums:
            pairs[num] += 1
            if pairs[num] == 2:
                pair_count += 1
                del pairs[num]

        return [pair_count, len(nums) - pair_count * 2]        
        