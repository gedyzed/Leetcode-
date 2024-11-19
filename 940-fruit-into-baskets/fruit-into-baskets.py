class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = left = treeCount = 0
        trees = defaultdict(int)

        for right in range(len(fruits)):
            if trees[fruits[right]] == 0:
                treeCount += 1

            trees[fruits[right]] += 1 

            while treeCount > 2:
                trees[fruits[left]] -= 1 
                if trees[fruits[left]] == 0:
                    treeCount -= 1
                left += 1        
                
            max_fruits = max(max_fruits, right - left + 1)   

        return max_fruits        


        