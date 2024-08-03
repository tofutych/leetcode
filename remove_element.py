class Solution(object):
    def removeElement(self, nums, val):
        s = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
                s += 1
        return s
