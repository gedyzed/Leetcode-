class Solution:
    def partitionLabels(self, nums: str) -> List[int]:
        dct = Counter(nums)
        ans = []
        st = set()
        l, r = 0, 0
        while r < len(nums):
            st.add(nums[r])
            dct[nums[r]] -= 1
            if dct[nums[r]] == 0:
                st.remove(nums[r])
            if len(st) == 0:
                ans.append(r - l + 1)
                l = r + 1
            r += 1
        return ans
        
        