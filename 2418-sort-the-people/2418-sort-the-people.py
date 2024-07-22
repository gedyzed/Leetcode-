class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peopleHeights = {}
        for i in range(len(names)):   
            peopleHeights[heights[i]] = names[i]

        peopleHeights = dict(sorted(peopleHeights.items(), reverse=True))  

        return peopleHeights.values()




        