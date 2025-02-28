class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_ = {}
        for index,  char in enumerate(order):
            order_[char] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):

                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_[words[i][j]] > order_[words[i + 1][j]]:
                        return False
                    break    
                  
        return True                       
     