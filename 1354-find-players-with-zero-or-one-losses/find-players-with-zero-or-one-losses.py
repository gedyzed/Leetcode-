class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        win_count = defaultdict(int)
        lose_count = defaultdict(int)

        for winner, loser in matches:
            win_count[winner] += 1
            lose_count[loser] += 1

        winners = sorted([w for w in win_count.keys() if lose_count[w] == 0])  
        losers = sorted([l for l in lose_count.keys() if lose_count[l] == 1]) 

        return [winners, losers] 



        