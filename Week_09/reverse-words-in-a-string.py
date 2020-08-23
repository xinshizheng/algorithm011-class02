class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = [[]]
        for c in s:
            if c == ' ':
                tmp.append([])
            else:
                tmp[-1] += c
        tmp = [''.join(i) for i in tmp[::-1] if i]
        return ' '.join(tmp)
