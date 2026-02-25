class Solution:
    def areAlmostEqual(self, s1, s2):
        
        # If already equal
        if s1 == s2:
            return True
        
        diff = []
        
        # Find mismatched indices
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        
        # Must have exactly two mismatches
        if len(diff) != 2:
            return False
        
        i, j = diff
        
        # Check if swapping makes strings equal
        return s1[i] == s2[j] and s1[j] == s2[i]
