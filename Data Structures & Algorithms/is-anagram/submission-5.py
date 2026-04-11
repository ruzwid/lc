class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}

        for l in s:
            d[l] = d.get(l, 0) + 1
        
        for l in t:
            d2[l] = d2.get(l, 0) + 1
        
        if d != d2:
            return False
        return True