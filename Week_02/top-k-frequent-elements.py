class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        return [v for _, v in heapq.nlargest(k, [(v, k) for k, v in hashmap.items()], key=lambda x: x[0])]
