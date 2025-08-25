class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        elements = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                elements[r + c].append(mat[r][c])

        res = []
        values = elements.values()
        for i, element in enumerate(values):
            if i > 0 and i & 1 == 0:
                res.extend(element[::-1])
            else:
                res.extend(element)    

        return res        


    



        