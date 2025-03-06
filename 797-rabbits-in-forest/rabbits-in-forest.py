class Solution:
    def numRabbits(self, answers: List[int]) -> int:

   
        total_rabbits = 0
        for x, freq in Counter(answers).items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            total_rabbits += groups * group_size
        
        return total_rabbits

            
        