class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        def mapIndex(words):
            word_index = {}
            for i, word in enumerate(words):
                word_index[word] = i

            return word_index   

        list1_count =  mapIndex(list1)
        list2_count =  mapIndex(list2) 

        common_strings = {}
        for key, value in list1_count.items():
            if key in list2_count:
                common_strings[key] = value + list2_count[key]


        min_count = min(list(common_strings.values()))    
        return [word for word, v in common_strings.items() if min_count == v]     


               
                


        