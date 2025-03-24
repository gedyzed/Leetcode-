class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = set(zip(s, t))
        return len(set(s)) == len(set(t)) == len(mappings)