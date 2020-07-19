class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if (not g) or (not s): return 0
        g.sort()
        s.sort()
        count = 0
        for i in g:
            for j in s:
                if j >= i:
                    s.remove(j)
                    count += 1
                    break
        return count
