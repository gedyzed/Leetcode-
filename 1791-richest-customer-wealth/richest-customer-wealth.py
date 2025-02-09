class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        richest = 0
        for account in accounts:
            richest = max(sum(account), richest)

        return richest    
        