class Solution:
    def binaryGap(self, n: int) -> int:
        b_nums = bin(n)[2:]
        left = right = max_len = 0

        for right in range(len(b_nums)):
            if b_nums[right] == '1' and b_nums[left] == '1':
                max_len = max(max_len, right - left)
                left = right
            elif b_nums[right] == '1' and b_nums[left] != '1':
                left = right

        return max_len        










        