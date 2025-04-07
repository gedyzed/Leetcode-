class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1:
            return 1

        trusts = set()
        not_trust = defaultdict(int)
        for p1, p2 in trust:

            trusts.add(p1)
            if p1 in not_trust:
                not_trust.pop(p1)
            if p2 not in trusts:
                not_trust[p2] += 1

        judge = list(not_trust.keys())
        count = list(not_trust.values())
        
        if not judge:
            return - 1
        return judge[0] if count[0] == n - 1 else -1
     
          

