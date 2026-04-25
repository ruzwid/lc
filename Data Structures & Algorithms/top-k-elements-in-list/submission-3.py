class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
    
        bucket = {}
        for i in range(len(nums)+1):
            bucket[i] = []
        # bucket = {i: [] for i in range(k+1)}


        for element, freq in count.items():
            bucket[freq].append(element)
        
        result = []
        
        for i in range(len(nums), 0, -1):
            if bucket[i]:
                for j in bucket[i]:
                    result.append(j)
                    if len(result) == k:
                        return result
        
        return result

        # O(n), O(n)