class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        curr_gain = total_gain = 0 
        start = 0
        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            if total_gain < 0:
                total_gain = 0
                start = i + 1

        return start 