class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        score = [(sc, idx) for idx, sc in enumerate(score)]
        score.sort(reverse=True)
        medals = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal", 
        }
        n = len(score)
        ans = ["1"] * n
        for i, sc in enumerate(score):
            rank = str(i + 1) 
            if rank in medals:
                ans[sc[1]] = medals[rank]
            else:    
                ans[sc[1]] = rank

        return ans     


       



        