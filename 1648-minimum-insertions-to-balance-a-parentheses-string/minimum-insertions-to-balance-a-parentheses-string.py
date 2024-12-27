class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []  # Stack to track unmatched '('
        count = 0   # Tracks the number of insertions needed
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                stack.append('(')  # Push unmatched '(' to the stack
            else:  # s[i] == ')'
                # Check if this is a single ')' or part of a pair '))'
                if i + 1 < len(s) and s[i + 1] == ')':
                    # It's part of a pair '))'
                    i += 1  # Move to the next character
                else:
                    # It's a single ')', so one more ')' is needed
                    count += 1  # Add one ')' to make it a pair
                
                # Try to match the '))' with a '(' from the stack
                if stack:
                    stack.pop()  # Match with a '('
                else:
                    count += 1  # No '(' to match, so one '(' is needed
            
            i += 1  # Move to the next character
        
        # At the end, each unmatched '(' in the stack needs 2 ')'
        count += len(stack) * 2
        return count
