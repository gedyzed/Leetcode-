class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        chars = defaultdict(int)

        for right in range(len(s)):
            chars[s[right]] += 1

            while any(count > 2 for count in chars.values()):
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
