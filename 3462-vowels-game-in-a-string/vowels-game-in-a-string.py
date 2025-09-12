class Solution:
    def doesAliceWin(self, s: str) -> bool:

        s_count = Counter(s)
        count = 0
        for k, val in s_count.items():
            if k in ["a", "i", "u", "o", "e"]:
                count += val
                
        return count != 0        




        