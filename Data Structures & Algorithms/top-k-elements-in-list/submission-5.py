class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        bucket = {}
        for i in range(len(nums) + 1):
            bucket[i] = []
        
        for num, count in counts.items():
            bucket[count].append(num)
        # print(bucket)
        result = []
        for i in range(len(bucket)-1, 0, -1):
            # print(i)
            if bucket[i]:
                for res in bucket[i]:
                    result.append(res)
                    if len(result) == k:
                        return result
        
        return result
            