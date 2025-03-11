class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:


        happiness.sort(reverse=True)
        happiness_value = 0
        decrement = i = 0

        while k and i < len(happiness):
            happy = happiness[i]
            if happy < decrement:
                break

            happiness_value += happy - decrement
            decrement += 1  
            k -= 1
            i += 1

        return happiness_value        
        