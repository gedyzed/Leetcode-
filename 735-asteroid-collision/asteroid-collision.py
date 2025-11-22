class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            if stack and stack[-1] > 0 and asteroid < 0:
                is_equal = False
                abs_asteroid = abs(asteroid)
                while stack and stack[-1] > 0 and stack[-1] <= abs_asteroid:
                        popped = stack.pop()
                        if popped == abs_asteroid:
                            is_equal = True
                            break
            
                if not is_equal and (not stack or stack[-1] < 0):
                    stack.append(asteroid)
            
            else:
                stack.append(asteroid)
        
        return stack

        