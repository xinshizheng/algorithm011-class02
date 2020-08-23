class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), 2*k):
            remain_str = s[i:i+2*k]
            remain_len = len(remain_str)
            if remain_len < k:
                res.append(remain_str[::-1])
            else:
                res.append(s[i:i+k][::-1])
                res.append(s[i+k:i+2*k])
        return ''.join(res)
