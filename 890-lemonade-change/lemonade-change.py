class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        bills_count = defaultdict(int)
        for bill in bills:
            if bill == 10:
                if not bills_count[5]:
                    return False
                bills_count[5] -= 1    

            elif bill == 20:
                if bills_count[10] and bills_count[5]:
                    bills_count[10] -= 1
                    bills_count[5] -= 1
                elif bills_count[5] >= 3:
                    bills_count[5] -= 3    
                else:    
                    return False

            bills_count[bill] += 1
            
        return True                 
                          