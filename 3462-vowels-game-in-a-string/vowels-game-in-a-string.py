class Solution:
    def doesAliceWin(self, s: str) -> bool:

        s_count = Counter(s)
        count, vowels = 0, ["a", "i", "u", "o", "e"]
        for k, val in s_count.items():
            if k in vowels:
                count += val

        return count != 0        




        