class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if length == 1 and digits[0] == 0:
            return [1]
        last_d = digits[-1]
        if last_d == 9:
            digits[-1] = 0
            i = -2
            while -i<=length and digits[i]==9:
                digits[i] = 0
                i -= 1
            if -i > length:
                digits.insert(0, 1)
            else:
                digits[i] += 1
        else:
            digits[-1] += 1
        return digits