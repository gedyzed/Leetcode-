class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count = Counter(answers)  
        total_rabbits = 0

        for x, freq in count.items():
            group_size = x + 1
            groups_needed = math.ceil(freq / group_size)
            total_rabbits += groups_needed * group_size
        
        return total_rabbits

            
        