class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {num:idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            _idx = hashmap.get(target - num)
            if _idx is not None and _idx != idx:
                return [idx, _idx]