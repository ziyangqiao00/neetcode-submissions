class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            
        for j in t:
            if j not in counts:
                return False
            
            counts[j] -= 1

            if counts[j] <0:
                return False

        return True        