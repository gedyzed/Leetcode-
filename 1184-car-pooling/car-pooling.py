class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        count = [0] * 1002
        for psg, frm, to in trips:
            count[frm] += psg
            count[to] -= psg

        for i in range(1, len(count)):
            count[i] += count[i - 1]   
    
        for psg in count:
            if psg > capacity:
                return False
        return True    


        