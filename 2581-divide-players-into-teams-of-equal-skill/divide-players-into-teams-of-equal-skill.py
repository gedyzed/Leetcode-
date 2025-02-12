class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill_sum =  ( sum(skill) * 2 ) // len(skill)
        skill.sort()
        left, right = 0, len(skill) - 1

        chemistry = 0
        while left < right:
            if skill[left] + skill[right] != skill_sum:
                return -1

            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1

        return chemistry        
 

        