class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        max_trees = 0
        basket = defaultdict(int)
        left = 0
        for right in range(len(fruits)):
            basket[fruits[right]] += 1
            while len(basket.keys()) > 2 :
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1
            max_trees = max(right - left + 1 , max_trees)    

        return max_trees    



        