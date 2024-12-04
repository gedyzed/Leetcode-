class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        count = 0 
        min_operations = 101
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                count += 1
            if i + 1 >=  k:
                min_operations = min(min_operations, count)  
                if blocks[i - k + 1] == 'W':
                    count -= 1
                    
        return min_operations             

        