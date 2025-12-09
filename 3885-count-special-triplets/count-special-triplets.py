class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        forward = Counter(nums)
        back = defaultdict(int)
        count = 0
        for num in nums:
            curr_num = num * 2
            if num in forward:
                forward[num] -= 1
                
            if back[curr_num] and forward[curr_num]:
                count += back[curr_num] * forward[curr_num] 
        
            back[num] += 1

        mod = 10 ** 9 + 7
        return count % mod
