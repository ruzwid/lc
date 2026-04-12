class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            counts = [0] * 26
            for l in string:
                index = ord(l) - 97
                counts[index] += 1
            key = tuple(counts)
            # if key not in res:
            #     res[key] = []
            # res[key].append(string)
            res.setdefault(key, []).append(string)

        return list(res.values())
        
        