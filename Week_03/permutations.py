class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        if k == 0: return []
        if k == 1: return [nums]
        res = []
        def generate(perm, k):
            if k == 0:
                res.append(perm)
                return
            unused = set(nums) - set(perm)
            for num in unused:
                generate(perm+[num], k-1)
        generate([], k)
        return res
