class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        x = list(bin(x)[2:])
        y = list(bin(y)[2:])

        count = 0
        while x or y:
            if x and y:
                if x[-1] != y[-1]:
                    count += 1
                x.pop()
                y.pop()

            elif x  and not y :
                if x[-1] == '1':
                    count += 1
                x.pop()  
            elif y and not x:
                if y[-1] == '1':
                    count += 1
                y.pop() 

        return count              
                     