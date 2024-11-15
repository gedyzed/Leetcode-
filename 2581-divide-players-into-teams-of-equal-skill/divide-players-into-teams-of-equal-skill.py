class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        n = len(skill)
        totalSum = sum(skill)
        skillSum = totalSum * 2 // n
        count = defaultdict(int)
        pair_count = 0
        chemistry = 0

        for i in range(n):
            x = skillSum - skill[i]
            if x in count and count[x] > 0:   
                chemistry += x * skill[i]
                pair_count += 1
                count[x] -= 1
            else:
                count[skill[i]] += 1    
        if pair_count != n / 2:
            return -1
        return chemistry            