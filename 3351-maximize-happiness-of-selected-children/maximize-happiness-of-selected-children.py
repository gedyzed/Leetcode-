class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:


        happiness.sort(reverse=True)
        happiness_sum = decrement = i = 0

        for i in range(k):

            happiness_sum += max(happiness[i] - decrement, 0)
            decrement += 1

        return happiness_sum    

       
        