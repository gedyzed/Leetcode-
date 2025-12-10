class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        root = complexity[0]
        complexity = complexity[1:]
        for com in complexity:
            if com <= root:
                return 0

        mod = 10 ** 9 + 7
        return math.factorial(len(complexity)) % mod
        