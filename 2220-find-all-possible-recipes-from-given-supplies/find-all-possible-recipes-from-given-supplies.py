class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {}
        graph = defaultdict(list)

        for r, ing_list in zip(recipes, ingredients):
            indegree[r] = len(ing_list)
            for ing in ing_list:
                graph[ing].append(r)

        q = deque(supplies)
        res = []

        while q:
            item = q.popleft()
            if item in indegree:
                res.append(item)

            for nei in graph[item]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res
