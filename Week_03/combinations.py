class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n<1 or k<1 or n<k: return []
        res = []
        def generate(comb, k):
            if k == 0:
                res.append(comb)
                return
            if len(comb) == 0:
                for i in range(1, n+1):
                    generate(comb+[i], k-1)
            else:
                if n-comb[-1] > k-1:
                    for i in range(comb[-1]+1, n+1):
                        generate(comb+[i], k-1)
        generate([], k)
        return res
