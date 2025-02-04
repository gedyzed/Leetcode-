class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]] :
 
        for i, path in enumerate(paths):
            paths[i] = path.split()

        root_name = defaultdict(list)     
        names = []  
        for path in paths:
            root = path[0] + '/' if path[0][-1] != '/' else path[0] 
            for j in range(1, len(path)):
                names.append(root + path[j])
        
        content_name = defaultdict(list)

        for i, name in enumerate(names):
            n = name.split('(')
            content_name[n[1]].append(n[0])

        return [n for n in content_name.values() if len(n) > 1]

            

 
        
  




        