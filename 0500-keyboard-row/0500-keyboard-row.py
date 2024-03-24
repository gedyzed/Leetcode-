class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "asdfghjkl"  
        secondRow = "qwertyuiop"
        thirdRow = "zxcvbnm"
    
        str1 = ""
        ans = ""
        answer = []
        
        
        for i in range (len(words)):
            str1 = words[i].lower()
            for j in range(len(str1)):
                s = str1[j]
                if s in firstRow:
                    ans = callRow(str1,firstRow)
                    break
                elif s in secondRow:
                    ans = callRow(str1,secondRow)
                    break
                else:  
                    ans = callRow(str1,thirdRow)
                    break
                    
            if str1 == ans:
                answer.append(words[i])
            
        return answer  
def callRow(str1,rows):
    firstRow = rows
    s = ""
    ans = ""
    for i in range(len(str1)):
        s = str1[i]
        if s in firstRow:
            ans += s
    return ans
