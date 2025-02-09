class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        def average(i, j):
            sum = count = 0
            row, col = len(img), len(img[0])

            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if 0 <= r < row and 0 <= c < col:
                        sum += img[r][c]
                        count += 1   
            return sum // count             


        mat = []
        for row in range(len(img)):
            m = []
            for col in range(len(img[0])):
                m.append(average(row, col))
            mat.append(m)    

        return mat        


        