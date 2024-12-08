class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list (s)
        for i in range(len(spaces)):
            s[spaces[i]] = " " + s[spaces[i]] 

        return "".join(s)