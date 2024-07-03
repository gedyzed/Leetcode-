class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        for char in t:
              count[char] -= 1 
               
        count_sum = 0
        for value in count.values():
            count_sum += abs(value)
            
        return not count_sum    

        