class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        left = 0
        stack = []
        answer = ''
        for right in range(len(word)):
            stack.append(word[right])
            if word[right] == ch:
                while stack:
                    answer += stack.pop()
                return answer + word[right+1:]
        return word






        