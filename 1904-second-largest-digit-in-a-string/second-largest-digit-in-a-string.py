class Solution:
    def secondHighest(self, s: str) -> int:

        s = list(set(s))
        nums = []
        for char in s:
            if char.isdigit():
                heappush(nums, int(char))

        res = nlargest(2, nums)
        print(res)
        return res[-1] if len(res) > 1 else -1     


        