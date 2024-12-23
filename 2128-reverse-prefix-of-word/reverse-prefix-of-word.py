class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        def reverse(right):
            result = ""
            while right >= 0:
                result += word[right]
                right -= 1    
            return result + word[len(result):]   

        index = 0
        for i in range(len(word)):
            if word[i] == ch: 
                index = i
                break

        return  reverse(index)
              





        