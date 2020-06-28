class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for num in nums2:
            for i in range(j, len(nums1)):
                if nums1[i] > num:
                    nums1.pop()
                    nums1.insert(i, num)
                    j = i + 1
                    m += 1
                    break
                elif i >= m:
                    nums1.pop()
                    nums1.insert(m, num)
                    m += 1
                    break