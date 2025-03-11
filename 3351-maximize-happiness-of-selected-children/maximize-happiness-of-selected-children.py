class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:


        happiness.sort(reverse=True)
        happiness_sum = 0

        for i in range(k):
            happiness_sum += max(happiness[i] - i, 0)

        return happiness_sum    

       
        