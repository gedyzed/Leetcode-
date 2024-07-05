class Solution(object):
    def countGoodSubstrings(self, s):
        left = 0
        right = 0
        count = 0
        while left + 1  < len(s) and right+1 < len(s):
            # Check if the third element i.e right + 1
            # is equal to the 1st/2nd elements
            # If so reset the window
            if s[right] == s[right + 1] or s[right+1] == s[left]:
                left += 1
                right = left
                continue
            else:
                right += 1
            if right - left == 2:
                count += 1
                left = left + 1
                right = left
        return count