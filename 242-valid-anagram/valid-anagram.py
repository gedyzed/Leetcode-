class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s, t = Counter(s), Counter(t)
        return s == t

        