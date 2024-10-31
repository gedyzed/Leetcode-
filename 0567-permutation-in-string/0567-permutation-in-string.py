class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        
        # Early return if s1 is longer than s2, because it can't be a substring
        if len_s1 > len_s2:
            return False
        
        # Count the characters in s1
        s1_count = Counter(s1)
        # Initialize the first window count of size len_s1 in s2
        window_count = Counter(s2[:len_s1])
        
        # Check if the initial window matches
        if s1_count == window_count:
            return True
        
        # Start sliding the window
        for i in range(len_s1, len_s2):
            # Add the next character to the window
            window_count[s2[i]] += 1
            # Remove the character that's no longer in the window
            window_count[s2[i - len_s1]] -= 1
            
            # Clean up zero-count entries to keep it comparable with s1_count
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
            
            # Check if the current window matches the character count of s1
            if window_count == s1_count:
                return True
        
        return False

    
        
        