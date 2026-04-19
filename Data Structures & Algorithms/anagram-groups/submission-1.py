class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            arr = [0] * 26
            for l in string:
                index = ord(l) - 97
                arr[index] += 1
            key = tuple(arr)
            res.setdefault(key, []).append(string)
        
        return list(res.values())

            