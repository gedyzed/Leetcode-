class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        s = Counter(s)
        values = list(s.values())
        for i, value in enumerate(values):
            if i + 1 < len(values) and value != values[i + 1]:
                return False
        return True     

        

        