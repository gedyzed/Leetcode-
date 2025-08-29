class Solution:
    def flowerGame(self, n: int, m: int) -> int:

        even_n, even_m = n // 2, m // 2  
        odd_n = (n // 2) + 1 if n % 2 else n // 2
        odd_m = (m // 2) + 1 if m % 2 else m // 2

        return even_n * odd_m + even_m * odd_n
