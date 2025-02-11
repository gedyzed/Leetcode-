class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        me = len(piles) - 2
        bob = max_coins = 0

        while bob < me:
            max_coins += piles[me]
            bob += 1
            me -= 2
            
        return max_coins     


        