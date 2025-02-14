class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t = Counter(t)
        window = defaultdict(int)
        required = len(t)
        accuqired = left = 0
        sol = (-1, len(s) + 1)

        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == t[s[right]]:
                accuqired += 1

            while accuqired == required:
                if sol[1] - sol[0] > right - left:
                    sol = (left, right)
                window[s[left]] -= 1    
                if window[s[left]] < t[s[left]]:
                    accuqired -= 1
                left += 1

        return s[sol[0]: sol[1] + 1] if sol[0] != -1 else ""            


        