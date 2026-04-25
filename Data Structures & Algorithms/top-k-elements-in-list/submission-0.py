class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_by_freq = sorted(list(count.items()), key=lambda x: x[1])

        top_k = sorted_by_freq[-k:]

        return [element for element, freq in top_k]