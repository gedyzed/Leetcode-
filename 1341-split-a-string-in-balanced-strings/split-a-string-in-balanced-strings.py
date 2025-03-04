class Solution:
    def balancedStringSplit(self, s: str) -> int:

        char_count = {"R" : 0, "L" : 0 }
        count = 0
        for char in s:
            char_count[char] += 1
            if char_count["R"] == char_count["L"]:
                count += 1
                
        return count        
        