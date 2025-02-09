class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for row in range(len(image)):
            for col in range(len(image[0])):
                image[row][col] = 1 if not image[row][col] else 0

        for row in range(len(image)):
            image[row].reverse()
            
        return image            

        