class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        me = len(piles) - 2
        bob = 0
        max_coins = 0
        while bob < me :
            max_coins += piles[me]
            me -= 2
            bob += 1
            
        return max_coins     



