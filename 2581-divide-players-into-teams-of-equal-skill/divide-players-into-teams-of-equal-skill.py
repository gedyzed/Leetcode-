class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        n = len(skill)
        totalSum = sum(skill)
        skillSum = totalSum * 2 // n
        chemistry = 0
        skill.sort()
        left, right = 0, n - 1 

        pairs = {}
        while left < right:
            if skill[left] + skill[right] != skillSum:
                return -1
            chemistry += skill[left] * skill[right]    
            left += 1
            right -= 1

        return chemistry    




        