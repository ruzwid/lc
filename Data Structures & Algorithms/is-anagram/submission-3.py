class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        base = ord('a')

        for n in range(len(s)):
            count[ord(s[n]) - base] += 1
            count[ord(t[n]) - base] -= 1

        for n in count:
            if n != 0:
                return False

        return True

# Time: O(n)
# Space: O(1)
