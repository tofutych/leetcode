    def maxSubArray(self, nums):
        newNum = maxTotal = nums[0]
        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)
        return maxTotal


nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums=nums))
