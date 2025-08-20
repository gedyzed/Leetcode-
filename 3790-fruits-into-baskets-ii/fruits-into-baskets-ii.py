class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        unplaced = len(fruits)
        taken = defaultdict(int)
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if not taken[i] and fruit <= basket:
                    taken[i] = fruit
                    unplaced -= 1    
                    break      

        return unplaced     





        