class Solution:
    def frequencySort(self, s: str) -> str:

        letters = Counter(s)
        sorted_letters = dict(sorted(letters.items(), key=lambda item : item[1], reverse=True))
        result = (k * v for k, v in sorted_letters.items())
        return "".join(result)
        
        