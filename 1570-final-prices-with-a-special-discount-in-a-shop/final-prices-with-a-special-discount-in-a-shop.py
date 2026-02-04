class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []
        ans = [0] * len(prices)
        for i, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                p, idx = stack.pop()
                ans[idx] = p - price

            stack.append((price, i))

        while stack:
            p, i = stack.pop()
            ans[i] = p
        
        return ans

       
        