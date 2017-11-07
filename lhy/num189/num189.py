class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:]=nums[-k:]+nums[:-k]
