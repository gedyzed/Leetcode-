class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]] :

        for i, path in enumerate(paths):
            paths[i] = path.split() 

        names = []  
        for path in paths:
            for j in range(1, len(path)):
                names.append(f"{path[0]}/{path[j]}")   
        
        content_name = defaultdict(list)
        for i, name in enumerate(names):
            file_name, content = name.split('(')
            content_name[content].append(file_name)

        return [n for n in content_name.values() if len(n) > 1]

            

 
        
  




        