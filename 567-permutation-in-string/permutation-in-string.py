class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dict_s1 = Counter(s1)
        dict_s2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):

            dict_s2[s2[right]] += 1
            if right >= len(s1) - 1:
                if dict_s1 == dict_s2:
                    return True
                char = s2[left]    
                dict_s2[char] -= 1
                if not dict_s2[char]:
                    del dict_s2[char] 
                left += 1    

        return False               



        