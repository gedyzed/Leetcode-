class Solution:
    def numRabbits(self, answers: List[int]) -> int:

   
        total_rabbits = 0
        count = Counter(answers)
        for x, freq in count.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            total_rabbits += groups * group_size
        
        return total_rabbits

            
        