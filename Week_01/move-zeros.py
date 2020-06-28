class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
                
        # if not any(nums):
        #     return
        # count = 0
        # while nums[0] == 0:
        #     nums.pop(0)
        #     count += 1
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         count += 1
        # nums[:] = nums + [0]*count