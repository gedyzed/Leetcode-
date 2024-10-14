class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        left = 0
        stack = []
        
        for right in range(len(word)):   
            stack.append(word[right])
            
            if word[right] == ch:
                stack.reverse()
                return ''.join(stack) + word[right+1:]
        return word






        