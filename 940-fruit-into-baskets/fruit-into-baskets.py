class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = max_len = 0
        fruits_c = defaultdict(int)
        for right, fruit in enumerate(fruits):
            fruits_c[fruit] += 1

            while len(fruits_c) > 2:
                fruit = fruits[left]
                fruits_c[fruit] -= 1
                if not fruits_c[fruit]:
                    del fruits_c[fruit]
                left += 1    

            max_len = max(max_len, right - left + 1)     
        return max_len     

        