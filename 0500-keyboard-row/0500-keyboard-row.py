class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "asdfghjkl"  
        secondRow = "qwertyuiop"
    
        str1 = ""
        ans = ""
        answer = []
        
        
        for i in range (len(words)):
            str1 = words[i].lower()
            for j in range(len(str1)):
                s = str1[j]
                if s in firstRow:
                    ans = callFirstRow(str1)
                    break
                elif s in secondRow:
                    ans = callSecondRow(str1)
                    break
                else:  
                    ans = callThirdRow(str1)
                    break
                    
            if str1 == ans:
                answer.append(words[i])
            
        return answer  
def callFirstRow(str1):
    firstRow = "asdfghjkl"
    s = ""
    ans = ""
    for i in range(len(str1)):
        s = str1[i]
        if s in firstRow:
            ans += s
    return ans
def callSecondRow(str1):
    secondRow = "qwertyuiop"
    s = ""
    ans = ""
    for i in range(len(str1)):
        s = str1[i]
        if s in secondRow:
            ans += s
    return ans 
def callThirdRow(str1):
    secondRow = "zxcvbnm"
    s = ""
    ans = ""
    for i in range(len(str1)):
        s = str1[i]
        if s in secondRow:
            ans += s
    return ans  