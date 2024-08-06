class Solution:
    def maxSubArray(self, nums):
        new_num = max_total = nums[0]
        for i in range(1, len(nums)):
            new_num = max(nums[i], nums[i] + new_num)
            max_total = max(new_num, max_total)
        return max_total
